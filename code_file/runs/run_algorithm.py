"""
=================================================
run_algorithm.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

=================================================
"""

from code_file.model import Model
import csv
from code_file.helpers import replace_best
from code_file.algorithms.hillclimber import execute_hillclimber
from code_file.algorithms.annealing import run_simulated_annealing
import time


def run_simple(type_base, dataclass):
    """ """
    with open("output/histo_data.csv", "w") as output_file:
        start = time.time()
        while time.time() - start < 5:
            model = Model()

            if type_base == 0:
                model.baseline()

            if type_base == 1:
                model.greedy()

            writer = csv.writer(output_file)

            if model.score > dataclass.best_score:
                (
                    dataclass.best_traject,
                    dataclass.best_score,
                    dataclass.best_fraction,
                ) = replace_best(model.score, model.traject, model.fraction)

            score = model.score
            dataclass.all_data.append(score)
            writer.writerow([score])
            print(dataclass.best_score)
            print(len(dataclass.best_traject))
            current_time = time.time() - start
            print(current_time)
   


def run_hillclimber(type_base, type_hillclimber, dataclass):
    
    model = Model()
    if type_base == 0:
        model.baseline()
    if type_base == 1:
        model.greedy()

    (
        dataclass.best_traject,
        dataclass.best_score,
        dataclass.best_fraction,
        dataclass.all_data,
        dataclass.duration
    ) = execute_hillclimber(model, type_base, type_hillclimber)
    with open("output/histo_data.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(dataclass.all_data)
        writer.writerow(dataclass.duration)




def run_repeated_simulated_annealing(type_base, dataclass):
    model = Model()
    if type_base == 0:
        model.baseline()
    if type_base == 1:
        model.greedy()

    start = time.time()
    while time.time() - start < 5:
        traject, score, fraction, data, tmp = run_simulated_annealing(model, type_base, start)
        if score > dataclass.best_score:
            (
                dataclass.best_traject,
                dataclass.best_score,
                dataclass.best_fraction,
            ) = replace_best(score, traject, fraction)
        dataclass.all_data.extend(data)
        dataclass.counter += 1
        dataclass.duration.extend(tmp)
    with open("output/histo_data.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(dataclass.all_data)
        writer.writerow(dataclass.duration)
        

   
