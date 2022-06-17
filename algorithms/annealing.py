from helpers import quality_score
import random
import copy
from algorithms.greedy import make_greedy_traject
from algorithms.baseline import make_baseline_traject
        

def temperature(start_temperature, total_iterations, iteration):
    temperature = start_temperature - (start_temperature/total_iterations)* iteration
    return temperature

def chance(score_old, score_new, temperature):
    chance = 2 ** ((score_old - score_new) / temperature)
    return chance

def change_traject(model, t):
    time = model.time_dict[t]
    model.total_time -= time
    model.number_traject -= 1

    for connection in range(len(model.visited_connections[t])):
        model.visited_connections[t][connection].visit -= 1

    model.traject[t] = []
    quality_score(model)
    return model

def single_traject(model, t, key):
    station = random.choice(model.stations)
    if key == 2:
        latest_traject, time, connections = make_baseline_traject(station)
    
    if key == 3:
        latest_traject, time, connections = make_greedy_traject(station)

    model.traject[t] = latest_traject
    model.total_time += time
    model.time_dict[t] = time
    model.visited_connections[t] = connections
    model.number_traject += 1
    return model

def run_simulated_annealing(model, key):
    total_iterations = 2000
    for i in range(total_iterations):
        print(i)
        if i == 0:
            start_temperature = 1000 
            new_version = copy.deepcopy(model)
        else:
            index = random.randint(0, (len(change_version.traject) - 1))
            change_version = change_traject(change_version, index)
            new_model = single_traject(change_version, index, key)
            quality_score(new_model)
            r = random.random()
            chance_float = chance(new_version.score, change_version.score, current_temperature)
            if r > chance_float:
                new_version = copy.deepcopy(new_version)
            else:
                new_version = copy.deepcopy(change_version) 
        current_temperature = temperature(start_temperature, total_iterations, i)   
        print(new_version.score) 
    return new_version.traject, new_version.score, new_version.fraction