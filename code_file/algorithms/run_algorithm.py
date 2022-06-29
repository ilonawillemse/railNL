"""
=================================================
run_algorithm.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

A file that make the chosen algoritm run
=================================================
"""

from code_file.classes.model import Model
import csv
from code_file.helpers import replace_best
from code_file.algorithms.hillclimber import execute_hillclimber
from code_file.algorithms.annealing import run_simulated_annealing
import time
import numpy as np
from code_file.algorithms.depth_hillclimber import depth_hillclimber


def choose_base_model(type_base):
    model = Model()
    if type_base == 0:
        model.baseline()
    if type_base == 1:
        model.greedy()
    return model


def run_simple(type_base, dataclass):
    """
    run the base algorithm multiple times and save the best output
    """
    with open("output/histo_data.csv", "w") as output_file:
        start = time.time()
        while time.time() - start < dataclass.RUNNING_TIME:
            model = choose_base_model(type_base)

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


def run_repeated_hillclimber(type_base, type_hillclimber, dataclass):
    """
    Run hillclimber algorithm
    """
    model = choose_base_model(type_base)

    start = time.time()
    while time.time() - start < dataclass.RUNNING_TIME:
        (
            best_traject,
            best_score,
            best_fraction,
            data,
        ) = execute_hillclimber(model, type_base, type_hillclimber)

        dataclass.all_data.append(best_score)

        # keep track of the best output when multiple hillclimbers are run
        if best_score > dataclass.best_score:
            (
                dataclass.best_traject,
                dataclass.best_score,
                dataclass.best_fraction,
            ) = replace_best(best_score, best_traject, best_fraction)
        dataclass.plot_data.extend(data)

    with open("output/plot_data_hillclimber.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(dataclass.plot_data)
        writer.writerow(
            np.linspace(0, dataclass.RUNNING_TIME, len(dataclass.plot_data))
        )


def run_repeated_simulated_annealing(type_base, dataclass, max_temperature):
    """
    run the simulated annealing algorithm multiple times and save the best output
    """
    model = choose_base_model(type_base)

    start = time.time()
    while time.time() - start < dataclass.RUNNING_TIME:
        traject, score, fraction, data = run_simulated_annealing(
            model, type_base, max_temperature
        )

        dataclass.all_data.append(score)

        # keep track of the best output when multiple simulated annealings are run
        if score > dataclass.best_score:
            (
                dataclass.best_traject,
                dataclass.best_score,
                dataclass.best_fraction,
            ) = replace_best(score, traject, fraction)
        dataclass.plot_data.extend(data)
        dataclass.counter += 1

    with open("output/plot_data_annealing.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(dataclass.plot_data)
        writer.writerow(
            np.linspace(0, dataclass.RUNNING_TIME, len(dataclass.plot_data))
        )

def run_repeated_depth_hillclimber(type_base, dataclass):
    """
    Run hillclimber algorithm
    """
    model = choose_base_model(type_base)

    start = time.time()
    while time.time() - start < dataclass.RUNNING_TIME:
        (
            best_traject,
            best_score,
            best_fraction,
        ) = depth_hillclimber(model)

        dataclass.all_data.append(best_score)

        # keep track of the best output when multiple hillclimbers are run
        if best_score > dataclass.best_score:
            (
                dataclass.best_traject,
                dataclass.best_score,
                dataclass.best_fraction,
            ) = replace_best(best_score, best_traject, best_fraction)

