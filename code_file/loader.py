"""
=================================================
loader.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Loads the station and connection data from database (csv file)
Adds the station objects with corresponding name, xcor and ycor to a list
Adds the connections between the stations to a dictionary with the connection number as key
=================================================
"""

from code_file.classes.connection import Connection
from code_file.classes.station import Station
import csv


def load_stations():
    """
    Loads the stations from database and add them to a list of stations
    """

    stations = []
    with open("data/data_nationaal/StationsNationaal.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            name = row[0]
            xcor = row[1]
            ycor = row[2]
            stations.append(Station(name, xcor, ycor))
        f.close()

    return stations


def add_connections(stations):
    """
    Adds the connections of the stations to a dictionary with the connection number as key
    """
    
    all_connections = {}

    with open("data/data_nationaal/ConnectiesNationaal.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        next(csv_reader)
        all_lines = []

        for lines in csv_reader:
            all_lines.append(lines)

        for i in range(len(all_lines)):
            for station in stations:
                if station.name == all_lines[i][0]:
                    for station2 in stations:
                        if station2.name == all_lines[i][1]:
                            all_connections[i] = Connection(
                                station, station2, all_lines[i][2], i
                            )
                            station.connections[i] = all_connections[i]
                            station2.connections[i] = all_connections[i]

    return all_connections
