import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_audio(filename, duration, fs=16000):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(filename, fs, recording)
    print("Recording saved to", filename)

for i in range(1,50):
    record_audio(f'audio_data/read/read{i}.wav', duration=2)
