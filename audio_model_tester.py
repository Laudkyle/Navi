import numpy as np
import sounddevice as sd
from tensorflow.keras.models import load_model
import librosa

# Define the commands and load the trained model
commands = ['person', 'read']  # Add your actual commands here
model = load_model('model.h5')
sr = 16000  # Sampling rate
n_mfcc = 13  # Number of MFCC features
fixed_length = 2  # Fixed length in seconds for each chunk
window_stride = 0.5  # Window stride in seconds

# Initialize variables for buffering audio data
audio_buffer = np.array([])

def preprocess_audio(audio, sr=16000, n_mfcc=13, fixed_length=2):
    y = librosa.util.fix_length(audio, size=sr * fixed_length)  # Ensure audio is 2 seconds
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def predict_command(audio_data):
    # Preprocess the audio input
    mfccs = preprocess_audio(audio_data, sr=sr, n_mfcc=n_mfcc, fixed_length=fixed_length)
    mfccs = mfccs[..., np.newaxis]  # Add channel dimension
    mfccs = np.expand_dims(mfccs, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(mfccs)
    predicted_label = np.argmax(predictions, axis=1)
    predicted_command = commands[predicted_label[0]]

    # Return the predicted command
    return predicted_command

def audio_callback(indata, frames, time, status):
    global audio_buffer

    if status:
        print(f"Status: {status}")

    try:
        # Append the new audio data to the buffer
        audio_buffer = np.concatenate((audio_buffer, indata.flatten()))

        # Calculate how many complete fixed-length segments we have in the buffer
        chunks_available = audio_buffer.shape[0] // (sr * fixed_length)

        if chunks_available > 0:
            for i in range(chunks_available):
                # Extract a fixed-length segment for processing
                segment = audio_buffer[i * sr * fixed_length:(i + 1) * sr * fixed_length]

                # Ensure segment length matches expected size
                if len(segment) == sr * fixed_length:
                    predicted_command = predict_command(segment)
                    print(f'Predicted Command: {predicted_command}')
                else:
                    print(f"Ignoring segment of incorrect length: {len(segment)}")

            # Remove the processed segments from the buffer
            audio_buffer = audio_buffer[chunks_available * sr * fixed_length:]

    except Exception as e:
        print(f"Error in audio_callback: {e}")

# Start streaming audio and predicting in real-time
blocksize = int(sr * window_stride)
with sd.InputStream(callback=audio_callback, channels=1, samplerate=sr, blocksize=blocksize):
    print("Listening... Press Ctrl+C to stop.")
    try:
        while True:
            pass  # Keep the stream open
    except KeyboardInterrupt:
        print("Stopped.")
