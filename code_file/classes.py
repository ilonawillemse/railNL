"""
=================================================
classes.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Station and Connection classes for the railway model
Stations have a name, xcor and ycor and know the adjacent connecting stations
Connections know the starting and ending stations with their corresponding duration time
to travel the connection and an id
=================================================
"""


class Station:
    "Station Object"

    def __init__(self, name, xcor, ycor):
        self.name = name
        self.connections = {}
        self.xcor = xcor
        self.ycor = ycor


class Connection:
    def __init__(self, station_1, station_2, time, id):
        self.start = station_1
        self.end = station_2
        self.visit = 0
        self.duration = time
        self.id = id


class Dataclass:
    def __init__(self):
        self.best_score = 0
        self.counter = 0
        self.best_fraction = 0
        self.best_traject = 0
        self.best_traject = []
        self.all_data = []
