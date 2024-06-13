import os
import librosa
import numpy as np
from tensorflow.keras.models import load_model
import sounddevice as sd
from functions import play_sound  # Assuming this is a function to play sounds

# Define the commands and speakers
commands = ['person', 'read']
speakers = ['Barak','Joe']  # Add your actual speaker names here

def record_audio(duration=2, sr=16000):
    play_sound('open')  # Optional: Play sound to indicate recording start
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    play_sound('close')  # Optional: Play sound to indicate recording end
    audio = audio.flatten()
    return audio

def preprocess_audio_from_array(audio, sr=16000, n_mfcc=13, fixed_length=2):
    y = librosa.util.fix_length(audio, size=sr * fixed_length)  # Ensure audio is 2 seconds
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def predict_from_audio(audio, model):
    # Preprocess the recorded audio
    mfccs = preprocess_audio_from_array(audio)
    mfccs = mfccs[np.newaxis, ..., np.newaxis]  
    
    # Predict using the model
    predictions = model.predict(mfccs)
    command_label = np.argmax(predictions[0])
    speaker_label = np.argmax(predictions[1])
    
    return command_label, speaker_label

# Load the trained model
model = load_model('Speaker_model.h5')  # Replace with your actual model path

# Record a 2-second audio clip
audio = record_audio(duration=2, sr=16000)

# Predict command and speaker
command_label, speaker_label = predict_from_audio(audio, model)

# Get command and speaker names
predicted_command = commands[command_label]
predicted_speaker = speakers[speaker_label]

print(f'Predicted Command: {predicted_command}')
print(f'Predicted Speaker: {predicted_speaker}')
