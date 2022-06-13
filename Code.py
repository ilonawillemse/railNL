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
import matplotlib.pyplot as plt
from visualize import visualization


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
        

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = []
        self.score = 0
        self.fraction = 0
        self.number_traject = 0
        self.total_time = 0
        self.traject = []
        self.time_dict = {}
        self.all_connections = {}
    

    def fraction_visited(self):
        "calculated fraction of visited stations"
        
        visited_connections = 0
        for connection in self.all_connections:
            if self.all_connections[connection].visit != 0:
                visited_connections += 1

        self.fraction = visited_connections / len(self.all_connections)
        

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
            

            for i in range(len(all_lines)):
                for station in self.stations:
                    if station.name == all_lines[i][0]:
                        for station2 in self.stations:
                            if station2.name == all_lines[i][1]:
                                self.all_connections[i] = Connection(station, station2, all_lines[i][2], i)
                                station.connections[i] = self.all_connections[i]
                                station2.connections[i] = self.all_connections[i]           

    def make_traject(self, station):
        time = 0
        visited_stations = []
        visited_stations.append(station)

        while time <= 120:
            connections = list(station.connections.values())
            

            new_choice = self.choose_connection(connections)
            if station.name != new_choice.start:
                new_station = new_choice.start
            else:
                new_station = new_choice.end
            

            counter = 0

            while new_station in visited_stations and counter < 100:
                new_choice = self.choose_connection(connections)
                new_choice.visit += 1
                if station != new_choice.start:
                    new_station = new_choice.start
                else:
                    new_station = new_choice.end
                counter += 1
                

            if counter == 100:
                break

            time += int(new_choice.duration)

            if time > 120:
                 time -= int(new_choice.duration)
                 break        

            station = new_station
            visited_stations.append(station)
        
        return visited_stations, time

    def get_name(self, list):
        names_list = []
        for i in range(len(list)):
            names_list.append(list[i].name)
        return names_list


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
        self.number_traject = random.randint(1,7)
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

                    

def repeated_runs():
    all_scores = []
    highest_score = 0
    with open('histo_data.csv', 'w') as output_file:
        for i in range(1000000):
            model = Model()
            model.load_stations()
            model.add_connections()
            model.run()
            writer = csv.writer(output_file) 
            if model.score > highest_score:
                best_traject = model.traject
                highest_score = model.score
            score = model.score
            all_scores.append(score)
            writer.writerow([score])
            print(i)

    with open('output/best_traject_output.csv', 'w') as output_best_file:
            writer = csv.writer(output_best_file)
            writer.writerow(['train', 'stations'])

            for i in range(len(best_traject)):
                names = model.get_name(best_traject[i])
                data = [f'train_{i+1}', names]
                writer.writerow(data)
                            
            writer.writerow(['score', format(highest_score, '.3f')])
    data = all_scores
    num_bins = 100 # <- number of bins for the histogram
    plt.hist(data, num_bins)
    plt.savefig("histogramtest.png")

    return best_traject 
            



if __name__ == "__main__":
    best_traject = repeated_runs()
            
    # model = Model()
    # model.load_stations()
    # model.add_connections()
    # model.run()

    # visualization(model, model.traject)
    
