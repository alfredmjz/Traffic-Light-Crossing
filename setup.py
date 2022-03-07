from time import sleep
import time
import numpy as np
from traffic import Traffic
from traffic_light import Traffic_Light, __init__


class Setup:
    '''
    This class initialize random default value for the environment of the 4-way traffic intersection.
    Running this will start the program.
    '''

    def __init__(self, traffic):
        '''
        Precondition:   Takes a list of exactly 4 Traffic_Light objects. Objects cannot be null
        Postcondition:  Each intersection will have a randomize number of traffic
                        Total traffic size is recorded
        Keywords:
        0   =   traffic_up
        1   =   traffic_right
        2   =   traffic_down
        3   =   traffic_left
        4   =   size of traffic
        '''
        traffic[0].number_of_traffic = np.random.randint(0, 10)
        traffic[1].number_of_traffic = np.random.randint(0, 10)
        traffic[2].number_of_traffic = np.random.randint(0, 10)
        traffic[3].number_of_traffic = np.random.randint(0, 10)
        traffic[4] = traffic[0].number_of_traffic + traffic[1].number_of_traffic + \
            traffic[2].number_of_traffic + traffic[3].number_of_traffic


if __name__ == '__main__':
    # Construct instances of Traffic_Light object for 4-way traffic intersection
    traffic_up = Traffic_Light("up")
    traffic_left = Traffic_Light("left")
    traffic_right = Traffic_Light("right")
    traffic_down = Traffic_Light("down")
    # Appends objects into list and intialize the environment
    traffic_size = 0
    traffic = [traffic_up,  traffic_right,
               traffic_down, traffic_left, traffic_size]
    setup = Setup(traffic)

    # Initialize the state of all drivers (Refer cars.py for states)
    cars_up = traffic[0].initialize_cars()
    cars_right = traffic[1].initialize_cars()
    cars_down = traffic[2].initialize_cars()
    cars_left = traffic[3].initialize_cars()
    cars = [cars_up, cars_right, cars_down, cars_left]

    # Start traffic light and move cars
    intersection = Traffic()
    current_lane = intersection.startTrafficLight(traffic)
    # Track the time taken to clear the intersection
    start_time = time.perf_counter()
    # Track the number of rotation taken to clear the intersection
    start_rotation = current_lane
    total_rotation = 0

    while (current_lane != -1):
        current_line_of_cars = cars[current_lane]
        intersection.moveCars(current_line_of_cars, traffic, current_lane)
        current_lane = intersection.changeTrafficLight(traffic, current_lane)
        line_of_cars = cars[current_lane]
        if(start_rotation == current_lane):
            total_rotation += 1

    elapsed_time = int(time.perf_counter() - start_time)
    print("Intersection is cleared.\nTotal time taken: {}s,\t Total rotation taken: {}".format(
        elapsed_time, total_rotation))
