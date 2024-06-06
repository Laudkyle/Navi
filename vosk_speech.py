import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# Initialize a queue to hold audio data
q = queue.Queue()

# Define the callback function to receive audio data from the microphone
def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))
# The model
model = Model("vosk")

# Initialize the recognizer
recognizer = KaldiRecognizer(model, 16000)

# Configure the audio stream
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening... Press Ctrl+C to stop.")

    while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            print("You said: ", result_dict.get("text", ""))
        else:
            partial_result = recognizer.PartialResult()
            partial_result_dict = json.loads(partial_result)
            print("Partial result: ", partial_result_dict.get("partial", ""))

