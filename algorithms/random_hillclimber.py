from helpers import quality_score
import random
import copy
from algorithms.greedy import make_greedy_traject
from algorithms.baseline import make_baseline_traject

def single_traject_random(model, t, key):

    for connection in range(len(model.visited_connections[t])):
        model.visited_connections[t][connection].visit -= 1

    station = random.choice(model.stations)
    if key == 2 or key == 6:
        latest_traject, time, connections = make_baseline_traject(station)
    
    if key == 3:
        latest_traject, time, connections = make_greedy_traject(station)

    model.traject[t] = latest_traject
    model.total_time -= model.time_dict[t]
    model.total_time += time
    model.time_dict[t] = time
    model.visited_connections[t] = connections
    return model

def random_hillclimber(model, key):
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
                    best_version = copy.deepcopy(best_version)
            else:
                best_version = copy.deepcopy(model)

            change_version = copy.deepcopy(best_version)
            random_index = random.randint(0, len(model.traject) - 1)
            new_model = single_traject_random(change_version, random_index, key)
            quality_score(new_model)
            counter += 1
            if counter % 500 == 0:
                print(counter)
                print(best_version.score, 'best 13')
            best_scores.append(best_version.score)
    except KeyboardInterrupt:
        pass
    return best_version.traject, best_version.score, best_version.fraction, best_scores





# def run_random_hillclimber(model, key):
#     unchanged_counter = 0
#     i = 0

#     while True:
#         if i > 0:
#             # print(new_model.score, "new")
#             # print(best_version.score, 'best')
#             if new_model.score >= best_version.score:
#                 best_version = copy.deepcopy(new_model)
#                 unchanged_counter = 0
#             else: 
#                 best_version = copy.deepcopy(best_version)
#                 unchanged_counter += 1
#         else:
#             best_version = copy.deepcopy(model)
#         changed_scores = []
#         for t in range(len(best_version.traject)):
#             copy_version = copy.deepcopy(best_version)      
#             removed_version = change_traject(copy_version, t)
#             changed_scores.append(removed_version.score)
            
#         change_version = copy.deepcopy(best_version) 
       
#         max_index = changed_scores.index(max(changed_scores))
               
#         change_version = change_traject(change_version, max_index)
#         new_model = single_traject(change_version, max_index, key)
#         quality_score(new_model)
#         i += 1
#         if unchanged_counter == 100:
#             return best_version.traject, best_version.score, best_version.fraction

