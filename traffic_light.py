from cars import *
from exception import *

class Traffic_Light:
    def __init__(self, direction):
        '''
        Precondition:   direction is a String argument of only ["up","left","right","down"]
        Postcondition:  Creates an instance of Traffic_Light object with the following variables

        Keywords:
        direction = direction of traffic light in a 4-way intersection (up,left,right or down)

        number_of_traffic = total number of cars waiting to pass the traffic

        red_light_timer = the timer for red light of the traffic light

        green_light_timer = the timer for green light of the traffic light

        status = current color of light of the traffic light
        '''
        try:
            if(bool(direction != "up") and bool(direction != "down") and bool(direction != "left") and bool(direction != "right")): 
                raise WrongValueError
            self.direction = direction
            self.number_of_traffic = 0
            self.red_light_timer = 0
            self.green_light_timer = 0
            self.status = 'red'
        except WrongValueError:
            print("{} is not accepted".format(direction),
            "direction can only be one of the following: ['up','left','right','down']",
            sep="\n")

    def initialize_cars(self):
        '''
        Creates and returns the list of cars based on the number_of_traffic of a specific direction
        Precondition:   Car object must have the same traffic direction
        Postcondition:  Returns a list of non-empty Car object with a given state
        '''

        inTraffic = []
        [inTraffic.append(Car()) for _ in range(self.number_of_traffic)]
        return inTraffic

    