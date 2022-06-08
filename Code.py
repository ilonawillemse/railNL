"""
=================================================
Code.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
=================================================
"""

import csv
import random


class Station():
    "Station Object"
    def __init__(self, name, xcor, ycor):
        self.name = name
        self.connections = {}
        self.visited = 0
        self.xcor = xcor
        self.ycor = ycor

    def is_visited(self):
        self.visited += 1
        

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = []
        self.traject = {}
        self.score = 0
        self.time = 0
    
    def fraction_visited(self):
        "calculated fraction of visited stations"
        counter = 0
        for station in self.stations:
            if station.visited == 0:
                counter += 1

        self.fraction = counter / len(self.stations)
        print(self.fraction)


    def add_time(self):
        for s in self.stations:
            for key, value in s.connections.items():
                self.time += int(value)


    def quality_score(self):
        "calculate quality score of model"
        # hardcode number of trajects
        T = 1
        quality = self.fraction * 10000 - (T * 100 + self.time)
        print(quality)
        return quality

    
    def load_stations(self):
        "load the stations from database"
        with open(f"data_holland/StationsHolland.csv") as f:

            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            
            for row in csv_reader:
                name = row[0]
                xcor = row[1]
                ycor = row[2]
                self.stations.append(Station(name, xcor, ycor))
            
            f.close()

    def add_connections(self):
        "add the connections of the stations"

        with open(f"data_holland/ConnectiesHolland.csv") as f:

            csv_reader = csv.reader(f, delimiter = ',')
            next(csv_reader)

            all_lines = []
            for lines in csv_reader:
                all_lines.append(lines)

            for station in self.stations:
                for connection in all_lines:
                    station_name = connection[0]
                    connection_name = connection[1]
                    distance = connection[2]
                    if station.name == station_name:
                        
                        for i in range(len(self.stations)):
                            if connection_name == self.stations[i].name:
                                station.connections[self.stations[i]] = distance
                                self.stations[i].connections[station] = distance

                    

    def make_traject(self):

        visited_stations = []
        station = random.choice(self.stations)
        visited_stations.append(station.name)
        station.visited += 1

        traject_length = random.randint(3, 12)

        for i in range(traject_length):
            connections = list(station.connections.keys())
            new_station = random.choice(connections)
            station = new_station
            visited_stations.append(station.name)
            station.visited += 1
            
        print(visited_stations)





if __name__ == "__main__":
    station = Model()

    station.load_stations()
    station.add_connections()
    station.make_traject()

    print(station.stations[20].name)
    print(list(station.stations[20].connections.keys())[0].name)
