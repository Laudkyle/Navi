import os
import librosa
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical


def preprocess_audio(file_path, sr=16000, n_mfcc=13, fixed_length=2):
    y, _ = librosa.load(file_path, sr=sr)
    y = librosa.util.fix_length(y, size=sr * fixed_length)  # Ensure audio is 2 seconds
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def load_data(dataset_path, sr=16000, n_mfcc=13, fixed_length=2):
    features = []
    command_labels = []
    speaker_labels = []
    
    speakers = os.listdir(dataset_path)
    speaker_id_map = {speaker: idx for idx, speaker in enumerate(speakers)}

    for speaker in speakers:
        speaker_path = os.path.join(dataset_path, speaker)
        if os.path.isdir(speaker_path):
            commands = os.listdir(speaker_path)
            for command in commands:
                command_path = os.path.join(speaker_path, command)
                if os.path.isdir(command_path):
                    files = os.listdir(command_path)
                    for file_name in files:
                        file_path = os.path.join(command_path, file_name)
                        mfccs = preprocess_audio(file_path, sr=sr, n_mfcc=n_mfcc, fixed_length=fixed_length)
                        features.append(mfccs)
                        command_labels.append(command)  # Store string command label
                        speaker_labels.append(speaker_id_map[speaker])

    # Convert command labels to numerical indices
    unique_commands = np.unique(command_labels)
    command_label_map = {label: idx for idx, label in enumerate(unique_commands)}
    command_labels = [command_label_map[label] for label in command_labels]

    features = np.array(features)
    command_labels = np.array(command_labels)
    speaker_labels = np.array(speaker_labels)

    return features, command_labels, speaker_labels, len(speakers)


def build_model(input_shape, num_classes_command, num_classes_speaker):
    # Input layer
    input_layer = Input(shape=input_shape)

    # Convolutional layers
    conv_layer1 = Conv2D(32, kernel_size=(3, 3), activation='relu')(input_layer)
    pooling_layer1 = MaxPooling2D(pool_size=(2, 2))(conv_layer1)
    dropout_layer1 = Dropout(0.25)(pooling_layer1)

    # Flatten for command classification
    flatten_layer_command = Flatten()(dropout_layer1)

    # Dense layers for command classification
    dense_layer_command1 = Dense(128, activation='relu')(flatten_layer_command)
    dropout_layer_command = Dropout(0.5)(dense_layer_command1)
    output_layer_command = Dense(num_classes_command, activation='softmax', name='command_output')(dropout_layer_command)

    # Flatten for speaker identification
    flatten_layer_speaker = Flatten()(dropout_layer1)

    # Dense layers for speaker identification
    dense_layer_speaker1 = Dense(128, activation='relu')(flatten_layer_speaker)
    dropout_layer_speaker = Dropout(0.5)(dense_layer_speaker1)
    output_layer_speaker = Dense(num_classes_speaker, activation='softmax', name='speaker_output')(dropout_layer_speaker)

    # Combine inputs and outputs into a model
    model = Model(inputs=input_layer, outputs=[output_layer_command, output_layer_speaker])

    # Compile model
    model.compile(loss={'command_output': 'categorical_crossentropy', 'speaker_output': 'categorical_crossentropy'},
                  optimizer='adam', metrics={'command_output': 'accuracy', 'speaker_output': 'accuracy'})

    return model


# Constants
sr = 16000  # Sampling rate
n_mfcc = 13  # Number of MFCC features
window_length = 2  # Window length in seconds
dataset_path = 'audio_data/speaker/'

# Load data
X, command_labels, speaker_labels, num_speakers = load_data(dataset_path, sr=sr, n_mfcc=n_mfcc, fixed_length=window_length)

# Convert labels to categorical
command_labels = to_categorical(command_labels)
speaker_labels = to_categorical(speaker_labels, num_speakers)

# Reshape data
input_shape = (n_mfcc, X.shape[2], 1)
X = X.reshape(X.shape[0], *input_shape)

# Split data
X_train, X_test, command_train, command_test, speaker_train, speaker_test = train_test_split(X, command_labels, speaker_labels, test_size=0.2, random_state=42)

# Build model
model = build_model(input_shape, len(np.unique(command_labels)), num_speakers)

# Train model
model.fit(X_train, {'command_output': command_train, 'speaker_output': speaker_train},
          epochs=20, batch_size=8, validation_data=(X_test, {'command_output': command_test, 'speaker_output': speaker_test}))

# Evaluate model
loss, command_accuracy, speaker_accuracy = model.evaluate(X_test, {'command_output': command_test, 'speaker_output': speaker_test})
print(f'Command Accuracy: {command_accuracy:.4f}')
print(f'Speaker Accuracy: {speaker_accuracy:.4f}')

model.save('Speaker_model.h5')
