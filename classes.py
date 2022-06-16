

class Station():
    "Station Object"
    def __init__(self, name, xcor, ycor):
        self.name = name
        self.connections = {}
        self.visited = 0
        self.xcor = xcor
        self.ycor = ycor

class Connection():
    def __init__(self, station_1, station_2, time, id):
        self.start = station_1
        self.end = station_2
        self.visit = 0
        self.duration = time
        self.id = id
        