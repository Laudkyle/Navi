import threading
import time
from datetime import datetime
import dateutil.parser
import logging
import math
import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
from functions import *
from tessaract import *
from person_recognition import *

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


# Configure logging
logging.basicConfig(filename='navi_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class State:
    def __init__(self, status):
        self.status = status

class Navi:
    def __init__(self, name, location, battery):
        self.name = name
        self.states = {}
        self.location = location
        self.current_state = None  # No initial state
        self.battery = battery
    
    def add_state(self, state_name, state_instance):
        self.states[state_name] = state_instance
        if not self.current_state:
            self.current_state = state_name
    
    def change_state(self, state_name):
        if state_name in self.states:
            self.current_state = state_name
        else:
            print(f"Error: State {state_name} not found.")
            
    def calibrate_steps(self):
        print("This function is used to calibrate meters into steps for users")

# Setting the setters
    def set_name(self, name):
        self.name = name
    
    def set_battery(self,battery):
        self.battery = battery 
         
    def set_location(self, location):
        self.location = location
        
# Setting the getters
    def get_state(self):
        return self.current_state
    
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_battery(self):
        return self.battery
    
    # Alrams and reminders
    
    def set_reminder(self, input_str):
        threading.Thread(target=self._run_reminder, args=(input_str,)).start()

    def set_alarm(self, input_str):
        threading.Thread(target=self._run_alarm, args=(input_str,)).start()

    def _run_reminder(self, input_str):
        try:
            reminder_time = dateutil.parser.parse(input_str)
            
            if reminder_time.date() == datetime.now().date():
                reminder_time = datetime.combine(datetime.now().date(), reminder_time.time())
            elif reminder_time < datetime.now():
                print("Error: Reminder time should be in the future.")
                return

            seconds_until_reminder = (reminder_time - datetime.now()).total_seconds()

            logging.info(f'Set reminder for {input_str} - Running')
            time.sleep(seconds_until_reminder)
            logging.info(f'Set reminder for {input_str} - Completed')
            print("Reminder: Time to do something!")

        except ValueError:
            print("Error: Unable to parse input for reminder.")
            logging.error(f'Error: Unable to parse input for reminder - {input_str}')

    def _run_alarm(self, input_str):
        try:
            alarm_time = dateutil.parser.parse(input_str)

            if alarm_time.date() == datetime.now().date():
                alarm_time = datetime.combine(datetime.now().date(), alarm_time.time())
            elif alarm_time < datetime.now():
                print("Error: Alarm time should be in the future.")
                return

            seconds_until_alarm = (alarm_time - datetime.now()).total_seconds()

            logging.info(f'Set alarm for {input_str} - Running')
            time.sleep(seconds_until_alarm)
            logging.info(f'Set alarm for {input_str} - Completed')
            print("Alarm: Wake up!")

        except ValueError:
            print("Error: Unable to parse input for alarm.")
            logging.error(f'Error: Unable to parse input for alarm - {input_str}')



class Idle(State):
    def chatbot(self):
        print("This is the idle function coordinator that will be first loaded when the model is loaded")
    def person_identification(self, navi):
        if navi.current_state == "Idle":
            print('This function identifies who stands in front of me and plural if necessary')
            logging.info(f"Command: Person Identification")
        else:
            print("Error: Cannot perform this function in the current state")
            logging.info(f"Command: Person Identification failed")
    def object_detection(self, navi):
        if navi.current_state == "Idle":
            print("This function detects if objects are present in a particular place")
        else:
            print("Error: Cannot perform this function in the current state")

    def color_identification(self, navi):
        if navi.current_state == "Idle":
            print("This function identifies any color in question.")
        else:
            print("Error: Cannot perform this function in the current state")

class Reading(State):
    def read_text(self, navi):
        if navi.current_state == "Reading":
            print("This function reads the text that is directed to the camera")
        else:
            print("Error: Cannot perform this function in the current state")

    def language_identification(self, navi):
        if navi.current_state == "Reading":
            print("This function identifies the language of a specific text in question")
        else:
            print("Error: Cannot perform this function in the current state")

    def translate(self, navi):
        if navi.current_state == "Reading":
            print("This function translates a specific text")
        else:
            print("Error: Cannot perform this function in the current state")

class Navigation(State):
    def path_detection(self, navi):
        if navi.current_state == "Navigation":
            print("This function is used for finding the path to use")
        else:
            print("Error: Cannot perform this function in the current state")

    def path_division(self, navi):
        if navi.current_state == "Navigation":
            print('This function is used to divide the found path into a number of sections')
        else:
            print("Error: Cannot perform this function in the current state")

    def path_decision(self,navi):
        if navi.current_state == "Navigation":
            print("This function is used to decide the path to take during navigation")
        else:
            print("Error: Cannot perform this function in the current state")


def execute_code(code, navi):
    try:
        result = eval(code, globals(), {'navi': navi})
        return result
    except Exception as e:
        return f"Error: {e}"

navi = Navi(name="Navie", location='Ghana', battery=100)

# Creating states with specific characteristics
idle_state = Idle(status="Idle")
read_state = Reading(status="Reading")
navigation_state = Navigation(status="Navigation")

# Adding states to Navi
navi.add_state(state_name="Idle", state_instance=idle_state)
navi.add_state(state_name="Reading", state_instance=read_state)
navi.add_state(state_name="Navigation", state_instance=navigation_state)

# Changing state and performing task
navi.change_state("Idle")

# Performing specific functions based on the current state
# idle_state.object_detection(navi)
# idle_state.person_identification(navi)
# idle_state.object_detection(navi)

# # Changing state and attempting to perform functions not in the current state
# navi.change_state("Navigation")
# idle_state.object_detection(navi) 
# idle_state.person_identification(navi)


# while True:
#     user_input = input("Ask a question (type 'exit' to end): ")
#     if user_input.lower() == 'exit':
#         break

#     if user_input.lower().startswith('set reminder'):
#         _, input_str = user_input.split(maxsplit=3)[2:]
#         navi.set_reminder(input_str)
#     elif user_input.lower().startswith('set alarm'):
#         _, input_str = user_input.split(maxsplit=3)[2:]
#         navi.set_alarm(input_str)
#     else:
#         code_to_execute = f'navi.{user_input.lower()}()'
#         result = execute_code(code_to_execute, navi)
#         print(result)

# Configuring the audio stream
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',channels=1, callback=callback):
    play_sound('open') 
    while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            user_input =  result_dict.get("text", "")
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == "read":
                speak(extract_text_from_image(text_capture_image()))
                
                navi.change_state("Idle")
            elif user_input.lower() == "who is this":
                speak(recognize_face_from_image(face_capture_image()))
                navi.change_state("Idle")

            elif user_input.lower() == "what color is this":
                speak(detect_color())
                navi.change_state("Idle")
            else:
                print(user_input)
     