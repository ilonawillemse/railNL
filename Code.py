"""
=================================================
Code.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
=================================================
"""

import csv

class Station():
    "Station Object"
    def __init__(self, name, xcor, ycor):
        self.name = name
        self.connections = []
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
            for connection in s.connections:
                for key, value in connection.items():
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

            for row in csv_reader:
                all_lines.append(row)


            for station in self.stations:
                for connection in all_lines:
                    
                    station_name = connection[0]
                    connection_name = connection[1]
                    distance = connection[2]

                    if station.name == station_name:
                        station.connections.append({connection_name: distance})

                    if station.name == connection_name:
                        station.connections.append({station_name: distance})



if __name__ == "__main__":
    station = Model()
    station.load_stations()
    station.add_connections()

    # print(station.stations[0].name)

    "get the keys and values of the connections"
    # for s in station.stations:
    #     for connection in s.connections:
    #         for key, value in connection.items():
                # print(key, value)
                # print(key)
                # print(value)

    station.fraction_visited()
    station.add_time()
    station.quality_score()


