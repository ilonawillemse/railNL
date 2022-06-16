
import random


def make_traject(station):
        time = 0
        visited_stations = []
        visited_connections = []
        visited_stations.append(station)

        while time < 180:
            connections = list(station.connections.values())
            new_choice = random.choice(connections)
            if station != new_choice.start:
                new_station = new_choice.start
            else:
                new_station = new_choice.end

            counter = 0

            while new_station in visited_stations and counter < 100:
                new_choice = random.choice(connections)
                if station != new_choice.start:
                    new_station = new_choice.start
                else:
                    new_station = new_choice.end
                counter += 1
                

            if counter == 100:
                break

            time += int(float(new_choice.duration))

            if time > 180:
                 time -= int(float(new_choice.duration))
                 break        

            new_choice.visit += 1
            station = new_station
            visited_stations.append(station)
            visited_connections.append(new_choice)

        return visited_stations, time, visited_connections

def starting_trajects(model):
    model.number_traject = random.randint(1,20)
    for i in range(model.number_traject):
        station = random.choice(model.stations)
        latest_traject, time, connections = make_traject(station)
        model.traject.append(latest_traject)
        model.total_time += time
        model.time_dict[i] = time
        model.visited_connections.append(connections)

        