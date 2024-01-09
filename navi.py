# Classes
class Navi():
    def __init__(self,name,currentState,battery):
        self.name = name
        self.states = ['idle','recognition','navigation']
        self.currentState = self.states[0]
        self.battery = battery
    
    def changeState(self,state):
        self.currentState =self.states[state]
        
class State():
    def __init__(self,state,status):
        self.state = state
        self.status = status
    
    
        