"""
=================================================
hillclimber.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Implements a hillclimber algorithm to search for best score by creating trajects
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

    # misschien deze in reverse


def single_traject(model, t, type_base, type_hillclimber):
    if type_hillclimber == 0:
        for connection in range(len(model.visited_connections[t])):
            model.visited_connections[t][connection].visit -= 1
        model.total_time -= model.time_dict[t]

    station = random.choice(model.stations)
    if type_base == 0:
        latest_traject, time, connections = make_baseline_traject(station)

    if type_base == 1:
        latest_traject, time, connections = make_greedy_traject(station)

    model.traject[t] = latest_traject
    model.total_time += time
    model.time_dict[t] = time
    model.visited_connections[t] = connections
    if type_hillclimber == 1:
        model.number_traject += 1
    return model


def run_hillclimber(model, type_base, type_hillclimber):
    # unchanged_counter = 0
    try:
        best_scores = []
        counter = 0
        best_version = copy.deepcopy(model)
        while True:
            change_version = copy.deepcopy(best_version)
            if type_hillclimber == 1:
                changed_scores = []
                # -------------------------functie slechtste trein...............<--
                for i in range(len(best_version.traject)):
                    copy_version = copy.deepcopy(
                        best_version
                    )  # voorkom deze deepcopy, sla dus wel 'weggegooide' traject op
                    removed_version = change_traject(copy_version, i)
                    quality_score(removed_version)
                    changed_scores.append(removed_version.score)
                    # argmax (max en index)
                max_index = changed_scores.index(max(changed_scores))
                # -------------max_index returnen
                change_version = change_traject(change_version, max_index)
                new_model = single_traject(
                    change_version, max_index, type_base, type_hillclimber
                )

            elif type_hillclimber == 0:
                random_index = random.randint(0, len(model.traject) - 1)
                new_model = single_traject(
                    change_version, random_index, type_base, type_hillclimber
                )

            quality_score(new_model)
            if new_model.score >= best_version.score:
                best_version = new_model
            counter += 1
            if counter % 500 == 0:
                print(counter)
                print(
                    best_version.score,
                )
            best_scores.append(best_version.score)

    except KeyboardInterrupt:
        pickle.dump(best_version, open("saved", "wb"))
        pass

    return best_version.traject, best_version.score, best_version.fraction, best_scores
