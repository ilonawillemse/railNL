"""
=================================================
greedy.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Greedy constructive searching algorithm for trajects with lowest costs (shortest travel duration)
=================================================
"""

import random
from code_file.algorithms.baseline import check_end_start_station, change_model_parameters

MAX_TIME = 180


def next_shortest(station, visited_connections):
    """
    Looks for nexts shortest duration to next station where the connection has not yet been visited
    and adds this station to its traject
    """

    shortest_duration = None
    new_choice = None
    for _, value in station.connections.items():
        # look for connections that have not been visited yet
        if value not in visited_connections:
            if (
                shortest_duration is None
                or int(float(value.duration)) < shortest_duration
            ):
                shortest_duration = int(float(value.duration))
                new_choice = value
    return new_choice


def make_greedy_traject(station):
    """
    makes a traject based on a greedy (lowest duration) algorithm
    """

    visited_connections = []
    visited_stations = []
    time = 0

    # add current station to visited stations list
    visited_stations.append(station)

    while time <= MAX_TIME:
        new_choice = next_shortest(station, visited_connections)
        if new_choice is None:
            break
      
        new_station = check_end_start_station(station, new_choice)

        # generate time
        time += int(float(new_choice.duration))

        if time > MAX_TIME:
            time -= int(float(new_choice.duration))
            break

        # add station to visited stations
        station = new_station
        new_choice.visit += 1
        visited_stations.append(station)
        visited_connections.append(new_choice)

    return visited_stations, time, visited_connections


def get_started(model):
    """
    run the greedy algorithm
    """

    model.number_traject = random.randint(1, 20)
    for i in range(model.number_traject):
        station = random.choice(model.stations)
        latest_traject, time, connections = make_greedy_traject(station)
        model = change_model_parameters(model, latest_traject, time, connections, i)

    

