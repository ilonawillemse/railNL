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
        

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = []
        self.score = 0
        self.quality = 0
        self.fraction = 0
        self.number_traject = random.randint(1,4)
        self.total_time = 0
    

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
        self.quality = self.fraction * 10000 - (self.number_traject * 100 + self.total_time)
        return self.quality

    
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
        self.traject = []
        time_dict = {}
        self.total_time = 0
        time = 0

        for i in range(self.number_traject):
            visited_stations = []
            station = random.choice(self.stations)
            visited_stations.append(station)
            station.visited += 1

            traject_length = random.randint(1, 30)

            for _ in range(traject_length):
                connections = list(station.connections.items())

                new_choice = random.choice(connections)
                new_station = new_choice[0]
                new_distance = new_choice[1]


                counter = 0

                while new_station in visited_stations and counter < 100:
                    new_choice = random.choice(connections)
                    new_station = new_choice[0]
                    new_distance = new_choice[1]
                    counter += 1

                if counter == 100:
                    break

                time += int(new_distance)

                station = new_station
                visited_stations.append(station)
                station.visited += 1
            
            self.traject.append(visited_stations)  

            time_dict[f'train_{i+1}'] = int(time)
            self.total_time += time
            time = 0

        print(time_dict)
        # print(self.total_time)



    def get_name(self, list):
        for i in range(len(list)):
            list[i] = list[i].name
        return list


    def output_generate(self):
        with open('output.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['train', 'stations'])

            # print(self.traject)
            for i in range(len(self.traject)):
                self.traject[i] = self.get_name(self.traject[i])
                data = [f'train_{i+1}', self.traject[i]]
                writer.writerow(data)
            
            writer.writerow(['score', format(self.quality, '.3f')])


if __name__ == "__main__":
    station = Model()

    station.load_stations()
    station.add_connections()
    station.make_traject()

    station.quality_score()
    station.output_generate()


