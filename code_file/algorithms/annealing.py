"""
=================================================
annealing.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Repeatedly searching for other trajects based on the chance formula: 2** ((old score - new score) / temperature)
Trajects can have better or worse score than the previous best score, where
taking on a worse score is dependant on the chance, which depends on the temperature
=================================================
"""

from code_file.helpers import quality_score
import random
import copy
from code_file.algorithms.hillclimber import replace_traject


def temperature(start_temperature, total_iterations, iteration):
    """
    Calculating and returning the temperature per iteration,
    using a linear function
    """
    temperature = start_temperature - (
        (start_temperature / total_iterations) * iteration
    )
    return temperature


def chance(score_old, score_new, temperature):
    """
    Calculating the acceptance chance of a model version
    with a score worse than the best score
    """
    chance = 2 ** ((score_new - score_old) / temperature)
    return chance


def change_model(current_version, type_base):
    """
    Changes a random traject within a model and
    recalculates model parameters
    """

    # choosing a random traject to be changed
    index = random.randint(0, (len(current_version.traject) - 1))

    # copy the model to only make changes to the copy
    copy_version = copy.deepcopy(current_version)

    # replace traject and adapt model parameters
    new_model = replace_traject(copy_version, index, type_base, 0)

    # calculate new quality score
    quality_score(new_model)
    return new_model


def run_simulated_annealing(model, type_base):
    """
    Running a simulated annealing, takes a model and
    a base type algorithm as input, to change a traject based on
    this base type
    """

    # run the model unless tiher is an OverflowError
    try:

        # initializing parameters of the simulated annealing such
        # as the number of iterations, the temperature and a list to keep
        # track of all scores, to be able to plot
        scores = []
        total_iterations = 100000
        current_version = copy.deepcopy(model)
        best_version = copy.deepcopy(model)
        max_temperature = 25
        current_temperature = max_temperature

        # loops for every iteration
        for i in range(total_iterations):

            # calculating the current temperature
            current_temperature = temperature(max_temperature, total_iterations, i)

            # creating a new model
            new_model = change_model(current_version, type_base)

            # determining a random number and calculating the acceptance chance
            random_float = random.random()
            chance_float = chance(
                current_version.score, new_model.score, current_temperature
            )

            # when the newly generated model has a higher score than the best
            # version, replacing the current and best version with the
            # newly generated model
            if new_model.score > best_version.score:
                current_version = new_model
                best_version = new_model

            # if the score of the new model is lower than the best score
            # and the random float is lower than the chance, the new model
            # will be the next current version and thus a new starting point
            elif random_float < chance_float:
                current_version = new_model
            scores.append(current_version.score)

    # if the function reaches an OverflowError, do not execute but just pass and
    # go into the next iteration
    except OverflowError:
        pass

    return best_version.traject, best_version.score, best_version.fraction, scores
