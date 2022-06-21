
"""
=================================================
annealing.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

repeats searching for better trajects based on the formula: 2** ((old score - new score) / temperature)
=================================================
"""

from code_file.helpers import quality_score
import random
import copy
from code_file.algorithms.hillclimber import change_traject, single_traject

temp_list = []
        

def temperature(start_temperature, total_iterations, iteration):
    temperature = start_temperature - ((start_temperature/total_iterations) * iteration)
    return temperature

def temperature2(start_temperature, iteration):
    temperature = start_temperature * (0.997 ** iteration)
    return temperature

def chance(score_old, score_new, temperature):
    chance = 2 ** ((score_new - score_old) / temperature)
    return chance

#def chance2(score_old, score_new, temperature)

def run_simulated_annealing(model, choice):
    try:
        scores = []
        total_iterations = 500000
        current_version = copy.deepcopy(model)
        best_version = copy.deepcopy(model)
        max_temperature = 25
        current_temperature = max_temperature
        for i in range(total_iterations):
            current_temperature = temperature(max_temperature, total_iterations, i)   
            index = random.randint(0, (len(current_version.traject) - 1))
            copy_version = copy.deepcopy(current_version)
            change_version = change_traject(copy_version, index)
            new_model = single_traject(change_version, index, choice)
            quality_score(new_model)
            r = random.random()
            chance_float = chance(current_version.score, new_model.score, current_temperature)

            scores.append(current_version.score)
            if new_model.score >= best_version.score:
                current_version = new_model
                best_version = new_model
                

            elif r < chance_float:
                current_version = new_model

    except OverflowError:
        pass
            

    return best_version.traject, best_version.score, best_version.fraction, scores