"""
=================================================
annealing.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Repeatedly searching for other trajects based on the chance formula:
    2** ((old score - new score) / temperature)
Trajects can have better or worse score than the previous best score, where
taking on a worse score is dependant on the chance, which depends on the temperature
=================================================
"""

from code_file.algorithms.helpers import quality_score
import random
import copy
from code_file.algorithms.hillclimber import replace_traject

TOTAL_ITERATIONS = 30


def temperature(start_temperature, iteration):
    """
    Calculating and returning the temperature per iteration, using a linear function
    """
    temperature = start_temperature - (
        (start_temperature / TOTAL_ITERATIONS) * iteration
    )
    return temperature


def chance(score_old, score_new, temperature):
    """
    Calculating the acceptance chance of a model version
    with a score worse than the best current score
    """
    chance = 2 ** ((score_new - score_old) / temperature)
    return chance


def change_model(current_version, type_base):
    """
    Changes a random traject within a model and recalculates model parameters
    """

    # choosing a random traject to be changed
    index = random.randint(0, (len(current_version.traject) - 1))

    copy_version = copy.deepcopy(current_version)

    # replace traject and adapt model parameters
    new_model = replace_traject(copy_version, index, type_base, 0)

    # calculate new quality score
    quality_score(new_model)
    return new_model


def run_simulated_annealing(model, type_base, start, max_temperature):
    """
    Simulated annealing takes a model and a base type algorithm as input,
    changes a traject based on this base type algorithm
    """

    # run the model unless there is an OverflowError
    try:
        scores = []
        current_version = copy.deepcopy(model)
        best_version = copy.deepcopy(model)
        current_temperature = max_temperature

        # loops for every iteration
        for iteration in range(TOTAL_ITERATIONS):
            # calculating the current temperature
            current_temperature = temperature(max_temperature, iteration)

            # creating a new model
            new_model = change_model(current_version, type_base)

            # determining a random number and calculating the acceptance chance
            random_float = random.random()
            accepted_chance = chance(
                current_version.score, new_model.score, current_temperature
            )

            # when the new model has a higher quality score,
            # replace the best version model with the new model
            if new_model.score > best_version.score:
                current_version = new_model
                best_version = new_model

            # when the random generated float is lower than the acceptance chance,
            # the new model with lower quality score than the current score can be accepted too.
            elif random_float < accepted_chance:
                current_version = new_model
            scores.append(current_version.score)

    # when OverflowError, pass and go onto the next iteration
    except OverflowError:
        pass

    return (
        best_version.traject,
        best_version.score,
        best_version.fraction,
        scores,
    )
