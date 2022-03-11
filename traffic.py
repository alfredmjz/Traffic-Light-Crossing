from time import sleep
import numpy as np
from stop_watch import Stopwatch
from text_colors import TextColors


class Traffic:

    def display(self, traffic, active_lane):
        '''
        Prints the number of traffic on each intersection and the map of the road
        Precondition:   Traffic must be Traffic_Light object and cannot be empty
        Postcondition:  Prints intersection and number of remaining cars in the lanes

        >>> display(list_of_traffic,2)

                |        |
                |   1    |
        ________|        |________

               0          3
        ________          ________
                |        |
                |   7    |
                |        |

        '''
        if(active_lane == 0):
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                      "", TextColors.GREEN, traffic[active_lane].number_of_traffic, TextColors.RESET, ""),
                  sep="\n")
            print("________|{:<9}|________".format(""),
                  "\t\t\t",
                  "{}{:^13}{:^13}{}".format(
                TextColors.RED, traffic[3].number_of_traffic, traffic[1].number_of_traffic, TextColors.RESET),
                "________{:<11}________".format(""),
                sep="\n")
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                "", TextColors.RED, traffic[2].number_of_traffic, TextColors.RESET, ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                sep="\n")
        elif(active_lane == 1):
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                      "", TextColors.RED, traffic[0].number_of_traffic, TextColors.RESET, ""),
                  sep="\n")
            print("________|{:<9}|________".format(""),
                  "\t\t\t",
                  "{:^13}{}{:^13}{}{}".format(
                TextColors.RED, traffic[3].number_of_traffic, TextColors.GREEN, traffic[active_lane].number_of_traffic, TextColors.RESET),
                "________{:<11}________".format(""),
                sep="\n")
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                "", TextColors.RED, traffic[2].number_of_traffic, TextColors.RESET, ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                sep="\n")
        elif(active_lane == 2):
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                      "", TextColors.RED, traffic[0].number_of_traffic, TextColors.RESET, ""),
                  sep="\n")
            print("________|{:<9}|________".format(""),
                  "\t\t\t",
                  "{}{:^13}{:^13}{}".format(
                TextColors.RED, traffic[3].number_of_traffic, traffic[1].number_of_traffic, TextColors.RESET),
                "________{:<11}________".format(""),
                sep="\n")
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                "", TextColors.GREEN, traffic[active_lane].number_of_traffic, TextColors.RESET, ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                sep="\n")
        elif(active_lane == 3):
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                      "", TextColors.RED, traffic[0].number_of_traffic, TextColors.RESET, ""),
                  sep="\n")
            print("________|{:<9}|________".format(""),
                  "\t\t\t",
                  "{}{:^13}{}{:^13}{}".format(
                      TextColors.GREEN, traffic[active_lane].number_of_traffic, TextColors.RED, traffic[1].number_of_traffic, TextColors.RESET),
                  "________{:<11}________".format(""),
                  sep="\n")
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{}{:^9}{}|{:<8}".format(
                "", TextColors.RED, traffic[2].number_of_traffic, TextColors.RESET, ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                sep="\n")
        else:
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{:^9}|{:<8}".format(
                "", traffic[0].number_of_traffic, ""),
                sep="\n")
            print("________|{:<9}|________".format(""),
                  "\t\t\t",
                  "{:^13}{:^13}".format(
                traffic[3].number_of_traffic, traffic[1].number_of_traffic),
                "________{:<11}________".format(""),
                sep="\n")
            print("{:<8}|{:<9}|{:<8}".format("", "", ""),
                  "{:<8}|{:^9}|{:<8}".format(
                "", traffic[2].number_of_traffic, ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                "{:<8}|{:<9}|{:<8}".format("", "", ""),
                sep="\n")

    def startTrafficLight(self, traffic, stopwatch):
        '''
        Chooses a random side of the intersection and begins the rotation
        Precondition:   traffic is a list of Traffic_Light object and is not empty
        Postcondition:  Returns -1 iff traffic_size is 0, positive integer otherwise
        Invariant:      traffic_size != 0
        '''
        # If size of traffic = 0
        if (traffic[4] == 0):
            return -1

        # Choose a random lane to start the green light for the first time
        lane_to_start = np.random.randint(0, 3)
        traffic[lane_to_start].status = "green"
        traffic[lane_to_start].green_light_timer = stopwatch.start()
        return lane_to_start

    def changeTrafficLight(self, traffic, current_green_light, stopwatch):
        '''
        Change color of traffic light from red to green in clockwise rotation
        Precondition:   startTrafficLight must be called before this method
                        traffic is a list of Traffic_Light object and is not empty
        Postcondition:  Changes selected lane in clockwise rotation from red to green light
                        Changes previous green to red light
        Invariant:      traffic_size != 0
                        index >= 0 and index <= 3
        '''
        if (traffic[4] == 0):
            return -1
        index = current_green_light
        start_timer = traffic[index].green_light_timer

        traffic[index].green_light_timer = stopwatch.elapsedTime(start_timer)
        traffic[index].status = "red"

        # If current light is left intersection, next light is upper intersection
        if(index == 3):
            index = 0
        elif(index < 3):
            index += 1

        # Start timer for new green light
        traffic[index].green_light_timer = stopwatch.start()
        return index

    def moveCars(self, line_of_cars, traffic, current_lane, stopwatch):
        '''
        Moves car when the light is green and update length of traffic for each lane respectively
        Precondition:   startTrafficLight must be called before this method
                        traffic is a list of Traffic_Light object and is not empty
        Postcondition:  Number of cars in the intersection decreases until 0
        '''
        start_timer = traffic[current_lane].green_light_timer

        if(traffic[current_lane].number_of_traffic == 0):
            self.display(traffic, current_lane)
            seconds = 0

            print("No cars in lane...waiting for traffic light to pass")
            while(True):
                elapsed_time = stopwatch.elapsedTime(start_timer)
                if(elapsed_time > 6):
                    print("Changing traffic light.....")
                    break
                elif(elapsed_time == seconds):
                    print((7 - elapsed_time), "seconds left",
                          sep=' ', end='\r', flush=True)
                    seconds += 1
            return

        index = 0
        seconds = 0
        elapsed_time = 0
        duration = 0
        delay = 0

        honkNext = False

        length_of_line = traffic[current_lane].number_of_traffic

        while(True):
            if(elapsed_time > 6):
                print("Changing traffic light...")
                break

            if(elapsed_time == duration):
                duration += 1
                self.display(traffic, current_lane)

                if(elapsed_time == seconds and honkNext):
                    print(
                        "HONK..HONK. Driver is finally moving...Delayed: ", delay, " seconds")
                    honkNext = False
                print(7 - elapsed_time, "seconds left",
                      sep=' ', end='\r', flush=True)

            elif((elapsed_time == seconds) and (index <= length_of_line - 1) and (length_of_line >= 0)):
                delay = line_of_cars[index].delayOnGreen()
                traffic[current_lane].number_of_traffic -= 1
                traffic[4] -= 1
                index += 1
                seconds += 1 + delay
                honkNext = True if (delay > 0) else False

            elapsed_time = stopwatch.elapsedTime(start_timer)
