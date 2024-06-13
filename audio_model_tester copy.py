import numpy as np
import sounddevice as sd
import librosa
from tensorflow.keras.models import load_model
from queue import Queue

# Define the commands and load the trained model
commands = ['person', 'read']  # Add your actual commands here
model = load_model('model.h5')
sr = 16000  # Sampling rate
n_mfcc = 13  # Number of MFCC features
window_length = 2  # Window length in seconds
# Initialize variables for buffering audio data

def preprocess_audio(audio, sr=16000, n_mfcc=13):
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def predict_command(audio_data):
    # Preprocess the audio input
    mfccs = preprocess_audio(audio_data, sr=sr, n_mfcc=n_mfcc)
    mfccs = mfccs[..., np.newaxis]  # Add channel dimension
    mfccs = np.expand_dims(mfccs, axis=0)  # Add batch dimension

    # Make prediction using your existing model
    predictions = model.predict(mfccs)
    predicted_label = np.argmax(predictions, axis=1)
    predicted_command = commands[predicted_label[0]]

    # Return the predicted command
    return predicted_command

# Initialize variables for buffering audio data
audio_buffer = np.array([], dtype=np.float32)  # Initialize as empty float32 array

def preprocess_audio(audio, sr=16000, n_mfcc=13):
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def predict_command(audio_data):
    # Preprocess the audio input
    mfccs = preprocess_audio(audio_data, sr=sr, n_mfcc=n_mfcc)
    mfccs = mfccs[..., np.newaxis]  # Add channel dimension
    mfccs = np.expand_dims(mfccs, axis=0)  # Add batch dimension

    # Make prediction using your existing model
    predictions = model.predict(mfccs)
    predicted_label = np.argmax(predictions, axis=1)
    predicted_command = commands[predicted_label[0]]

    # Return the predicted command
    return predicted_command

def audio_callback(indata, frames, time, status):
    global audio_buffer

    # Print debug information
    print('Called')

    if status:
        print(f"Status: {status}")
    else:
        print("No status")

    try:
        # Append the new audio data to the buffer
        audio_buffer = np.concatenate((audio_buffer, indata.flatten()))

        # Process audio data in chunks of window_length seconds
        while len(audio_buffer) >= sr * window_length:
            # Extract a window_length segment for processing
            segment = audio_buffer[:sr * window_length]
            audio_buffer = audio_buffer[sr * window_length:]

            # Ensure segment length matches expected size
            if len(segment) == sr * window_length:
                # Perform prediction
                predicted_command = predict_command(segment)
                print(f'Predicted Command: {predicted_command}')
            else:
                print("Segment length does not match expected size")

    except Exception as e:
        print(f"Error in callback: {e}")

# Start streaming audio and predicting in real-time
blocksize = int(sr * 1)  # Adjust blocksize for better performance
with sd.InputStream(callback=audio_callback, channels=1, samplerate=sr, blocksize=blocksize):
    print("Listening... Press Ctrl+C to stop.")
    try:
        while True:
            pass  # Keep the stream open
    except KeyboardInterrupt:
        print("Stopped.")

