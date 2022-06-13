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
import visualize

class Station():
    "Station Object"
    def __init__(self, name, xcor, ycor):
        self.name = name
        self.connections = {}
        self.visited = 0
        self.xcor = xcor
        self.ycor = ycor
        

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = []
        self.score = 0
        self.fraction = 0
        self.number_traject = 7
        self.total_time = 0
        self.traject = []
        self.time_dict = {}
    

    def fraction_visited(self):
        "calculated fraction of visited stations"
        visited_stations = 0
        for station in self.stations:
            if station.visited != 0:
                visited_stations += 1

        self.fraction = visited_stations / len(self.stations)

    def quality_score(self):
        "calculate quality score of model"
        self.fraction_visited()
        self.score = self.fraction * 10000 - (self.number_traject * 100 + self.total_time)
        return self.score


    
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
                    

    def make_traject(self, station):
        time = 0
        visited_stations = []
        visited_stations.append(station)

        while time <= 120:
            connections = list(station.connections.items())

            new_choice = self.choose_connection(connections)
            new_station = new_choice[0]
            new_distance = new_choice[1]

            counter = 0

            while new_station in visited_stations and counter < 100:
                new_choice = self.choose_connection(connections)
                new_station = new_choice[0]
                new_distance = new_choice[1]
                counter += 1

            if counter == 100:
                break

            time += int(new_distance)

            if time > 120:
                 time -= int(new_distance)
                 break        

            station = new_station
            visited_stations.append(station)
        
        return visited_stations, time

    def get_name(self, list):
        for i in range(len(list)):
            list[i] = list[i].name
        return list


    def output_generate(self):
        with open('output.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['train', 'stations'])

            for i in range(len(self.traject)):
                names = self.get_name(self.traject[i])
                data = [f'train_{i+1}', names]
                writer.writerow(data)
            
            writer.writerow(['score', format(self.score, '.3f')])

    def choose_starting(self):
        station = random.choice(self.stations)
        return station
    
    def choose_connection(self, connections):
        return random.choice(connections)

    def set_visited(self):
        for station in self.stations:
            station.visited = 0

        for station in self.stations:
            for traject in self.traject:
                if station in traject:
                    station.visited += 1
    
    def starting_trajects(self):
        for i in range(self.number_traject):
            station = self.choose_starting()
            latest_traject, time = self.make_traject(station)
            self.traject.append(latest_traject)
            self.total_time += time
            self.time_dict[i] = time        

    def run(self):
        self.starting_trajects()

        self.set_visited()  
        self.quality_score()
        self.output_generate()


if __name__ == "__main__":
    model = Model()

    model.load_stations()
    model.add_connections()
    model.run()
