import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import sounddevice as sd
from functions import play_sound


commands = ['person', 'read']

def record_audio(duration=2, sr=16000):
    play_sound('open')
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    play_sound('close')
    audio = audio.flatten()
    return audio

def preprocess_audio_from_array(audio, sr=16000, n_mfcc=13, fixed_length=2):
    y = librosa.util.fix_length(audio, size=sr * fixed_length)  # Ensure audio is 2 seconds
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

# Record a 2-second audio clip
audio = record_audio(duration=2, sr=16000)

# Preprocess the recorded audio
mfccs = preprocess_audio_from_array(audio, sr=16000)
mfccs = mfccs[..., np.newaxis]  # Add channel dimension

# Load the trained model
model = load_model('model.h5')

# Add a batch dimension to the MFCCs
mfccs = np.expand_dims(mfccs, axis=0)

# Make predictions
predictions = model.predict(mfccs)
predicted_label = np.argmax(predictions, axis=1)

# Map the label to the corresponding command
predicted_command = commands[predicted_label[0]]

print(f'Predicted Command: {predicted_command}')
