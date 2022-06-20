from helpers import quality_score
import random
import copy
from algorithms.hillclimber import change_traject, single_traject
        

def temperature(start_temperature, total_iterations, iteration):
    temperature = start_temperature - (start_temperature/total_iterations)* iteration
    return temperature

def chance(score_old, score_new, temperature):
    chance = 2 ** ((score_old - score_new) / temperature)
    return chance

def run_simulated_annealing(model, key):
    total_iterations = 100000
    best_version = copy.deepcopy(model)
    for i in range(total_iterations):
        if i == 0:
            start_temperature = 1000 
            new_version = copy.deepcopy(model)
        else:
            index = random.randint(0, (len(new_version.traject) - 1))
            change_version = change_traject(new_version, index)
            new_model = single_traject(change_version, index, key)
            quality_score(new_model)
            r = random.random()
            chance_float = chance(new_version.score, change_version.score, current_temperature)
            if r > chance_float:
                new_version = copy.deepcopy(new_version)
            else:
                new_version = copy.deepcopy(change_version)
                if new_version.score > best_version.score:
                    best_version = copy.deepcopy(new_version)
        current_temperature = temperature(start_temperature, total_iterations, i)   
        print(best_version.score) 
    return new_version.traject, new_version.score, new_version.fraction