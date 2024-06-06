import speech_recognition as sr

def callback(recognizer, audio):
    try:
        # Perform speech recognition using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print(f"Google Speech Recognition thinks you said: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Capture microphone input
mic = sr.Microphone()

# Adjust for ambient noise
print("Adjusting for ambient noise, please wait...")
with mic as source:
    recognizer.adjust_for_ambient_noise(source)

print("Listening...")

# Start listening in the background (non-blocking)
stop_listening = recognizer.listen_in_background(mic, callback)

print("Listening in the background... Press Ctrl+C to stop.")

# Keep the program running indefinitely
try:
    while True:
        pass
except KeyboardInterrupt:
    stop_listening(wait_for_stop=False)
    print("Exiting the program.")
