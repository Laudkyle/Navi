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
class Idle(State):
    def chatbot(self):
        print("This is the idle function coordinator that will be first loaded when the model is loaded")
    def person_identification(self, navi):
        if navi.current_state == "Idle":
            print('This function identifies who stands in front of me and plural if necessary')
        else:
            print("Error: Cannot perform this function in the current state")

    def object_detection(self, navi):
        if navi.current_state == "Idle":
            print("This function detects if objects are present in a particular place")
        else:
            print("Error: Cannot perform this function in the current state")

    def object_identification(self, navi):
        if navi.current_state == "Idle":
            print("This function identifies any object in question. Colors too")
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
idle_state.object_detection(navi)
idle_state.person_identification(navi)
idle_state.object_identification(navi)

# Changing state and attempting to perform functions not in the current state
navi.change_state("Navigation")
idle_state.object_detection(navi) 
idle_state.person_identification(navi)


while True:
    user_input = input("Ask a question (type 'exit' to end): ")
    if user_input.lower() == 'exit':
        break

    code_to_execute = f'navi.{user_input.lower()}()'
    result = execute_code(code_to_execute, navi)
    print(result)
