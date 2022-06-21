"""
=================================================
random_hillclimber.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

implements a hillclimber algorithm to search for best score by creating trajects on a random base
=================================================
"""

from code_file.helpers import quality_score
import random
import copy
from code_file.algorithms.greedy import make_greedy_traject
from code_file.algorithms.baseline import make_baseline_traject
import pickle


def single_traject_random(model, t, choice):

    for connection in range(len(model.visited_connections[t])):
        model.visited_connections[t][connection].visit -= 1

    station = random.choice(model.stations)
    if choice == 0:
        latest_traject, time, connections = make_baseline_traject(station)
    
    if choice == 1:
        latest_traject, time, connections = make_greedy_traject(station)

    model.traject[t] = latest_traject
    model.total_time -= model.time_dict[t]
    model.total_time += time
    model.time_dict[t] = time
    model.visited_connections[t] = connections
    return model

def random_hillclimber(model, choice, N):
    try:
        best_scores = []
        counter = 0
        while True:
            if counter > 0:
                # print(new_model.score, "new")
                # print(best_version.score, 'best')
                if new_model.score >= best_version.score:
                    best_version = copy.deepcopy(new_model)

            else:
                best_version = copy.deepcopy(model)

            change_version = copy.deepcopy(best_version)

            if N == 1:
                random_index = random.randint(0, len(model.traject) - 1)
                new_model = single_traject_random(change_version, random_index, choice)
            
            elif N > 1:
                index_list = list(range(0, (len(model.traject))))
                
                indexes = random.choices(index_list, k=N)
                
                for index in indexes:
                    new_model = single_traject_random(change_version, index, choice)
                    change_version = copy.deepcopy(new_model)
                    


            quality_score(new_model)
            counter += 1
            if counter % 500 == 0:
                print(counter)
                print(best_version.score, 'best 10')
            best_scores.append(best_version.score)
    except KeyboardInterrupt:
        pickle.dump(best_version, open("saved", "wb"))
        pass
    return best_version.traject, best_version.score, best_version.fraction, best_scores