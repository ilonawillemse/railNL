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
        

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = []
        self.traject = {}
        self.score = 0
    
    def fraction_visited(self):
        pass
    
    def quality_score(self):
        pass
        # return p * 10000 - (T * 100 + Min)

    
    def load_stations(self):

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

    print(station.stations[0].name)


    # for connection in station.stations[0].connections:
    #     for distance in connection.values():
    #         print(distance)


    for s in station.stations:
        print(s.name)
        for connection in s.connections:
            for distance in connection.values():
                print(distance)



dict = {'a': 1}

