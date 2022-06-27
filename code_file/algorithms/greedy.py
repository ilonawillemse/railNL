"""
=================================================
greedy.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

greedy constructive searching algorithm for trajects with lowest costs (shortest travel duration)
=================================================
"""

import random


def next_shortest(station, visited_connections):
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
    visited_connections = []
    visited_stations = []
    time = 0

    # add current station to visited stations list
    visited_stations.append(station)

    while time <= 180:
        new_choice = next_shortest(station, visited_connections)
        if new_choice is None:
            break

        if station != new_choice.start:
            new_station = new_choice.start
        else:
            new_station = new_choice.end

        # counter = 0

        # while new_station in visited_stations and counter < 100:
        #     new_choice = next_shortest(station, visited_connections)
        #     if station != new_choice.start:
        #         new_station = new_choice.start
        #     else:
        #         new_station = new_choice.end
        #     counter += 1

        # if counter == 100:
        #     break

        # generate time
        time += int(float(new_choice.duration))

        if time > 180:
            time -= int(float(new_choice.duration))
            break

        # add station to visited stations
        station = new_station
        new_choice.visit += 1
        visited_stations.append(station)
        visited_connections.append(new_choice)

    return visited_stations, time, visited_connections


def get_started(model):
    model.number_traject = random.randint(1, 20)
    for i in range(model.number_traject):
        station = random.choice(model.stations)
        latest_traject, time, connections = make_greedy_traject(station)
        model.traject.append(latest_traject)
        model.total_time += time
        model.time_dict[i] = time
        model.visited_connections.append(connections)
