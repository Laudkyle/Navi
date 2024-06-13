

import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def preprocess_audio(file_path, sr=16000, n_mfcc=13, fixed_length=2):
    y, _ = librosa.load(file_path, sr=sr)
    y = librosa.util.fix_length(y, size=sr * fixed_length)  # Ensure audio is 2 seconds
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def load_data(commands, dataset_path, sr=16000, n_mfcc=13, fixed_length=2):
    features = []
    labels = []
    
    for idx, command in enumerate(commands):
        command_path = os.path.join(dataset_path, command)
        for file_name in os.listdir(command_path):
            file_path = os.path.join(command_path, file_name)
            mfccs = preprocess_audio(file_path, sr=sr, n_mfcc=n_mfcc, fixed_length=fixed_length)
            features.append(mfccs)
            labels.append(idx)
    
    features = np.array(features)
    labels = np.array(labels)
    return features, labels

commands = ['person', 'read']
X, y = load_data(commands, 'audio_data/')
print("Processed")

# Parameters
num_classes = len(commands)
n_mfcc = 13

# Reshape data
X = X.reshape(X.shape[0], n_mfcc, X.shape[2], 1)
y = to_categorical(y, num_classes)
print("shaped")
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(n_mfcc, X_train.shape[2], 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=20, batch_size=8, validation_data=(X_test, y_test))
model.save('model.h5')
# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy:.4f}')
