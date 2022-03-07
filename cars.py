import numpy as np
class Car:
    def __init__(self):
        '''
        Construct an instance of Car object with a randomized state
        Precondition:   The number of Car object to construct is equivalent to the number_of_traffic (refer to traffic_light.py)
        Postcondition:  Each Car object is given only ONE randomized state that is immutable
        '''
        state = { 0:"strict", 1:"tired", 2:"unattentive", 3:"distracted"}
        last_index = len(state) - 1
        selected = state[np.random.randint(0,last_index)]
        self.state = selected

    def delayOnGreen(self):
        '''
        Returns the potential delay of each Car object depending on its respective state
        Precondition:   current_state must not be null and can only be one of the 4 given states
        Postcondition:  delay is the number of seconds the current Car will take to pass the traffic on "green"
        Invariants:     current_state == 'strict'
                        current_state == 'tired' or 'unattentive'
                        current_state == 'distracted'
        '''
        current_state = self.state
        if current_state == 'strict':
            delay = 0
        elif current_state == 'tired':
            delay = 1
        elif current_state == 'unattentive' or 'distracted':
            delay = np.random.randint(2,3)
        return delay

