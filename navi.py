class Navi:
    def __init__(self, name,location, battery):
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

    def perform_task(self):
        if self.current_state:
            self.states[self.current_state].perform_task()
        else:
            print("Error: No state set.")
            
    def set_location(self,location):
        self.location = location

class State:
    def __init__(self, status):
        self.status = status
    
    def perform_task(self):
        pass  

class Idle(State):
    def person_identification(self):
        print('This function identifies who stand infront of me and plural in neccesary')
        
    def object_detection(self):
        print("This function detects if objects are present in a particular place")
        
    def object_identification(self):
        print("This function identify any object in question. Colors")

class Reading(State):
    def read_text(self):
        print("This function reads the text that is directed to the camera")
        
    def language_identification(self):
        print("This function identifies the language of a specific text in question")
        
    def translate(self):
        print("This function translates a specific text")
class Navigation(State):
     def perform_task(self):
        pass
    
# Example usage:
navi = Navi(name="Navie", battery=100)

# Creating states with specific characteristics
idle_state = Idle(status="Idle")
reading_state = Reading(status="Reading")
navigation_state = Navigation(status="Navigation")

# Adding states to Navi
navi.add_state(state_name="Idle", state_instance=idle_state)
navi.add_state(state_name="Reading", state_instance=reading_state)
navi.add_state(state_name="Navigation", state_instance=navigation_state)

# Changing state and performing task
navi.change_state("Idle")
navi.perform_task()

# Changing state and performing task
navi.change_state("Reading")
navi.perform_task()

# Changing state and performing task
navi.change_state("Navigation")
navi.perform_task()
