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

def check_end_start_station(station, new_choice):
    """
    Check if the new station is end or start station
    """
    if station != new_choice.start:
        new_station = new_choice.start
    else:
        new_station = new_choice.end
    return new_station

def change_model_parameters(model, latest_traject, time, connections, i):
    """
    Change model parameters after generating new model
    """
    model.traject.append(latest_traject)
    model.total_time += time
    model.time_dict[i] = time
    model.visited_connections.append(connections)
    return model

# def next(station, visited_connections):
#     new_choice = None
#     for _, value in station.connections.items():
#         if value not in visited_connections:
#             new_choice = value

#     return new_choice


def make_baseline_traject(station):
    """
    Creates new random traject
    """

    time = 0
    visited_stations = []
    visited_connections = []
    visited_stations.append(station)

    # ---------------------- limited connection use--------------
    # while time < MAX_TIME:
    #     new_choice = next(station, visited_connections)
    #     if new_choice == None:
    #         break

    #     if station != new_choice.start:
    #         new_station = new_choice.start
    #     else:
    #         new_station = new_choice.end

    # ------------------------ limited station use -----------------
    # add stations to the traject as long as the max duration of the traject is not yet reached
    while time <= MAX_TIME:
        connections = list(station.connections.values())
        new_choice = random.choice(connections)
        if new_choice is None:
            break

        new_station = check_end_start_station(station, new_choice)

        counter = 0

        # try finding stations that have not yet visited, if not found for 100 times quit
        while new_station in visited_stations and counter < 100:
            new_choice = random.choice(connections)
            new_station = check_end_start_station(station, new_choice)
            counter += 1

        if counter == 100:
            break
        # ---------------------------------------------------

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

    # model.number_traject = random.randint(7,13)
    model.number_traject = 11
    for i in range(model.number_traject):
        station = random.choice(model.stations)
        latest_traject, time, connections = make_baseline_traject(station)
        model = change_model_parameters(model, latest_traject, time, connections, i)


