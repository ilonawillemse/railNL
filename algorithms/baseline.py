
import random


def make_traject(station):
        time = 0
        visited_stations = []
        visited_stations.append(station)

        while time <= 120:
            connections = list(station.connections.values())
            new_choice = random.choice(connections)
            if station.name != new_choice.start:
                new_station = new_choice.start
            else:
                new_station = new_choice.end

            counter = 0

            while new_station in visited_stations and counter < 100:
                new_choice = random.choice(connections)
                new_choice.visit += 1
                if station != new_choice.start:
                    new_station = new_choice.start
                else:
                    new_station = new_choice.end
                counter += 1
                

            if counter == 100:
                break

            time += int(float(new_choice.duration))

            if time > 120:
                 time -= int(float(new_choice.duration))
                 break        

            station = new_station
            visited_stations.append(station)
        return visited_stations, time

def choose_starting(model):
    station = random.choice(model.stations)
    return station

def starting_trajects(model):
    model.number_traject = random.randint(1,20)
    for i in range(model.number_traject):
        station = choose_starting(model)
        latest_traject, time = make_traject(station)
        model.traject.append(latest_traject)
        model.total_time += time
        model.time_dict[i] = time