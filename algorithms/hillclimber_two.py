"""
=================================================
hillclimber_two.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

hillclimber replaces the two worst trajects with random new generated traject

!!not yet tested!!
=================================================
"""

from helpers import quality_score
import copy
from algorithms.hillclimber import change_traject, single_traject


def run_hillclimber(model, key):
    unchanged_counter = 0
    i = 0

    while True:
        if i > 0:
            if new_model.score >= best_version.score:
                best_version = copy.deepcopy(new_model)
                unchanged_counter = 0
            else: 
                best_version = copy.deepcopy(best_version)
                unchanged_counter += 1
        else:
            best_version = copy.deepcopy(model)
        changed_scores = []
        for t in range(len(best_version.traject)):
            copy_version = copy.deepcopy(best_version)      
            removed_version = change_traject(copy_version, t)
            changed_scores.append(removed_version.score)
            
        change_version = copy.deepcopy(best_version) 
       
        max_index = changed_scores.index(max(changed_scores))
        tmp = changed_scores.pop(max_index)
        second_value = max(tmp)
        second_index = changed_scores.index(second_value)
        change_version = change_traject(change_version, max_index)
        new_model = single_traject(change_version, max_index, key)

        change_version = change_traject(change_version, second_index)
        new_model = single_traject(change_version, second_index, key)        
        quality_score(new_model)
        i += 1
        if unchanged_counter == 100:
            return best_version.traject, best_version.score, best_version.fraction