"""
=================================================
baseline.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

creates railway trajects based on a random algorithm
bias:   max of 180 min traject length
        max station visit of one (total or per traject?)
=================================================
"""

import random

MAX_TIME = 180
MAX_TRIAL = 100


def make_baseline_traject(station):
    """
    Creates new random traject
    """

    time = 0
    visited_stations = []
    visited_connections = []
    visited_stations.append(station)

    # add stations to the traject as long as the max duration of the traject is not yet reached
    while time <= MAX_TIME:
        connections = list(station.connections.values())
        new_choice = random.choice(connections)
        if new_choice is None:
            break

        if station != new_choice.start:
            new_station = new_choice.start
        else:
            new_station = new_choice.end

        counter = 0

        # try finding stations that have not yet visited, if not found for 100 times quit
        while new_station in visited_stations and counter < MAX_TRIAL:
            new_choice = random.choice(connections)
            if station != new_choice.start:
                new_station = new_choice.start
            else:
                new_station = new_choice.end
            counter += 1

        if counter == MAX_TRIAL:
            break

        time += int(float(new_choice.duration))

        # if duration time of the traject has exceeded the maximum time, remove last added station
        if time > MAX_TIME:
            time -= int(float(new_choice.duration))
            break

        new_choice.visit += 1
        station = new_station
        visited_stations.append(station)
        visited_connections.append(new_choice)

    return visited_stations, time, visited_connections


def starting_trajects(model):
    """
    run the baseline (random) algorithm
    """

    model.number_traject = random.randint(7, 13)
    # model.number_traject = 11
    for i in range(model.number_traject):
        station = random.choice(model.stations)
        latest_traject, time, connections = make_baseline_traject(station)
        model.traject.append(latest_traject)
        model.total_time += time
        model.time_dict[i] = time
        model.visited_connections.append(connections)
