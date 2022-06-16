from helpers import quality_score
from algorithms.baseline import choose_starting
import random
import copy
        

def change_traject(model, t):
    time = model.time_dict[t]
    model.total_time -= time
    model.number_traject -= 1

    for connection in range(len(model.visited_connections[t])):
        model.visited_connections[t][connection].visit -= 1

    model.traject[t] = []
    quality_score(model)
    return model

def make_traject_hillclimber(station):
    time = 0
    visited_connections = []
    visited_stations = []
    visited_stations.append(station)

    while time <= 180:
        connections = list(station.connections.values())
        new_choice = random.choice(connections)
        if station.name != new_choice.start:
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
        visited_stations.append(new_station)
        visited_connections.append(new_choice)
        
    return visited_stations, time, visited_connections

def single_traject(model, t):
    station = choose_starting(model)
    latest_traject, time, connections = make_traject_hillclimber(station)
    model.traject[t] = latest_traject
    model.total_time += time
    model.time_dict[t] = time
    model.visited_connections[t] = connections
    model.number_traject += 1
    return model

def starting_trajects_hillclimber(model):
    model.number_traject = random.randint(1,20)
    for i in range(model.number_traject):
        station = choose_starting(model)
        latest_traject, time, connections = make_traject_hillclimber(station)
        model.traject.append(latest_traject)
        model.total_time += time
        model.time_dict[i] = time
        model.visited_connections.append(connections)

def run_hillclimber(model):
    for i in range(1000):
        if i > 0:
            print(new_model.score, "new")
            print(best_version.score, 'best')
            if new_model.score > best_version.score:
                best_version = copy.deepcopy(new_model)
            else: 
                print("hi")
                best_version = copy.deepcopy(best_version)
        else:
            best_version = copy.deepcopy(model)
        changed_scores = []
        for t in range(len(best_version.traject)):
            copy_version = copy.deepcopy(best_version)      
            removed_version = change_traject(copy_version, t)
            changed_scores.append(removed_version.score)
            
        change_version = copy.deepcopy(best_version) 
       
        max_index = changed_scores.index(max(changed_scores))
               
        change_version = change_traject(change_version, max_index)
        new_model = single_traject(change_version, max_index)
        quality_score(new_model)
    return best_version.traject, best_version.score, best_version.fraction
       

        
