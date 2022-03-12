import time


class Stopwatch:
    def __init__(self):
        self.startTime = 0

    def start(self):
        self.startTime = int(time.time())
        return self.startTime

    def elapsedTime(self):
        return int(time.time()) - self.startTime
