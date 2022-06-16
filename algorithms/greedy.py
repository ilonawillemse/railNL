
import random

def next_shortest(station):
    shortest_duration = None
    new_choice = None
    for _, value in station.connections.items():
        # look for connections that have not been visited yet
        if value.visit == 0:

            if shortest_duration == None or int(float(value.duration)) < shortest_duration :
                shortest_duration = int(float(value.duration))
                new_choice = value       
    return new_choice

def make_traject(station):
    visited_stations = []
    time = 0

    # add current station to visited stations list
    visited_stations.append(station)
    # print('begin', station.name)

    while time < 180:
        new_choice = next_shortest(station)
        if new_choice == None:
            break

        if station != new_choice.start:
            new_station = new_choice.start
        else:
            new_station = new_choice.end
       
        counter = 0
       
        while new_station in visited_stations:
            new_choice = next_shortest(station)
            if new_choice == None:
                break

            if station != new_choice.start:
                new_station = new_choice.start
            else:
                new_station = new_choice.end
            counter += 1

            if counter == 100:
                break
                            

        # generate time
        time += int(float(new_choice.duration))

        if time > 180:
            time -= int(float(new_choice.duration))
            break        

        # add station to visited stations 
        station = new_station
        new_choice.visit += 1
        visited_stations.append(station)
        # print(station.name)
        # print(time)

    
    return visited_stations, time

def get_started(model):
    station = random.choice(model.stations)
    model.number_traject = random.randint(1,20)
    for i in range(model.number_traject):
        # in case i would like to let trains drive same traject
        # for connection in model.all_connections.values():
        #     connection.visit = 0
        # print()
        # print(i)
        station = random.choice(model.stations)
        latest_traject, time = make_traject(station)
        model.traject.append(latest_traject)
        model.total_time += time
        model.time_dict[i] = time