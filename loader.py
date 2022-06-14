
from classes import Station, Connection
import csv

def load_stations():
    "load the stations from database"
    stations = []
    with open(f"data_holland/StationsHolland.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            name = row[0]
            xcor = row[1]
            ycor = row[2]
            stations.append(Station(name, xcor, ycor))
        f.close()
    return stations


def add_connections(stations):
    "add the connections of the stations"
    all_connections = {}
    #print(len(stations))
    with open(f"data_holland/ConnectiesHolland.csv") as f:

        csv_reader = csv.reader(f, delimiter = ',')
        next(csv_reader)

        all_lines = []
        for lines in csv_reader:
            all_lines.append(lines)
        
        for i in range(len(all_lines)):
            for station in stations:
                if station.name == all_lines[i][0]:
                    for station2 in stations:
                        if station2.name == all_lines[i][1]:
                            all_connections[i] = Connection(station, station2, all_lines[i][2], i)
                            station.connections[i] = all_connections[i]
                            station2.connections[i] = all_connections[i]
    #print(all_connections)
    return all_connections