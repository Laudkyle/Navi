import librosa
import numpy as np
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Load audio file
input_file = 'audio_data/long/read_long.wav'
output_dir = 'audio_data/read'

os.makedirs(output_dir, exist_ok=True)

# Load the audio file using librosa
y, sr = librosa.load(input_file, sr=None)

# Convert the numpy array to an AudioSegment
audio = AudioSegment(
    y.tobytes(), 
    frame_rate=sr,
    sample_width=y.dtype.itemsize, 
    channels=1
)

# Increase the silence threshold (e.g., dBFS-10 means less sensitivity to quieter silences)
silence_thresh = audio.dBFS - 10

# Split the audio where silence is 500ms or more and keep the chunks that are at least 1000ms long
chunks = split_on_silence(
    audio, 
    min_silence_len=500, 
    silence_thresh=silence_thresh,
    keep_silence=250
)

# Export each chunk as a separate file
for i, chunk in enumerate(chunks):
    chunk.export(os.path.join(output_dir, f"read_{i+1}.wav"), format="wav")

print(f"Saved {len(chunks)} commands to {output_dir}")