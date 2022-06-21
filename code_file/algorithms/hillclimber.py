"""
=================================================
hillclimber.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

implements a hillclimber algorithm to search for best score by creating trajects
=================================================
"""

from code_file.helpers import quality_score
import random
import copy
from code_file.algorithms.greedy import make_greedy_traject
from code_file.algorithms.baseline import make_baseline_traject
import pickle
        

def change_traject(model, t):

    time = model.time_dict[t]
    model.total_time -= time
    model.number_traject -= 1

    for connection in range(len(model.visited_connections[t])):
        model.visited_connections[t][connection].visit -= 1

    model.traject[t] = []
    
    return model

def single_traject(model, t, choice):
    station = random.choice(model.stations)
    if choice == 0:
        latest_traject, time, connections = make_baseline_traject(station)
    
    if choice == 1:
        latest_traject, time, connections = make_greedy_traject(station)

    model.traject[t] = latest_traject
    model.total_time += time
    model.time_dict[t] = time
    model.visited_connections[t] = connections
    model.number_traject += 1
    return model

def run_hillclimber(model, choice):
    #unchanged_counter = 0
    try:
        best_scores = []
        best_version = copy.deepcopy(model)
        while True:
            changed_scores = []
            for i in range(len(best_version.traject)):
                copy_version = copy.deepcopy(best_version)      
                removed_version = change_traject(copy_version, i)
                quality_score(removed_version)
                changed_scores.append(removed_version.score)
                
            change_version = copy.deepcopy(best_version) 
        
            max_index = changed_scores.index(max(changed_scores))
                
            change_version = change_traject(change_version, max_index)
            new_model = single_traject(change_version, max_index, choice)
            quality_score(new_model)

            if new_model.score >= best_version.score:
                best_version = new_model
            #     unchanged_counter = 0
            # else: 
            #     unchanged_counter += 1

            # print(best_version.score)
            # print(best_version.number_traject)
            # if unchanged_counter == 100:
            best_scores.append(best_version.score)
    except KeyboardInterrupt:
        pickle.dump(best_version, open("saved", "wb"))
        pass
    return best_version.traject, best_version.score, best_version.fraction, best_scores

                #return best_version.traject, best_version.score, best_version.fraction
