"""
=================================================
run_algorithm.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

A file that make the chosen algoritm run
=================================================
"""

from code_file.model import Model
import csv
from code_file.helpers import replace_best
from code_file.algorithms.hillclimber import run_hillclimber
from code_file.algorithms.annealing import run_simulated_annealing


def run_simple(type_base, dataclass):
    """
    run the base algorithm multiple times and save the best output
    """
    with open("output/histo_data.csv", "w") as output_file:
        try:
            while True:
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

        except KeyboardInterrupt:
            pass


def run_repeated_hillclimber(type_base, type_hillclimber, dataclass):
    """
    run the hillclimber algorithm
    """
    model = Model()

    # perform the chosen base type
    if type_base == 0:
        model.baseline()
    if type_base == 1:
        model.greedy()

    (
        dataclass.best_traject,
        dataclass.best_score,
        dataclass.best_fraction,
        dataclass.all_data,
    ) = run_hillclimber(model, type_base, type_hillclimber)


def run_repeated_simulated_annealing(type_base, dataclass):
    """
    run the simulated annealing algorithm multiple times and save the best output
    """
    model = Model()

    # perform the chosen base type
    if type_base == 0:
        model.baseline()
    if type_base == 1:
        model.greedy()

    try:
        # keep track of the best output when multiple simulated annealings are run
        while True:
            traject, score, fraction, data = run_simulated_annealing(model, type_base)
            if score > dataclass.best_score:
                (
                    dataclass.best_traject,
                    dataclass.best_score,
                    dataclass.best_fraction,
                ) = replace_best(score, traject, fraction)
            dataclass.all_data.extend(data)
            dataclass.counter += 1

    except KeyboardInterrupt:
        pass
