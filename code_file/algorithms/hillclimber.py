"""
=================================================
hillclimber.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Implements two hillclimber algorithms to search for best score by creating trajects:
- A hillclimber that removes the 'worst functioning' traject and replaces it
with a randomly generated traject
- A hillclimber that randomly removes a traject and replaces it with a randomly
generated traject
=================================================
"""

from code_file.helpers import quality_score
import random
import copy
import numpy as np
from code_file.algorithms.greedy import make_greedy_traject
from code_file.algorithms.baseline import make_baseline_traject


def change_model_parameters(model, index):
    """
    This function changes some of the models parameters
    corresponding to the removal of a certain traject
    """

    # looping over every connection of the specific traject (index) and substracts visited by one
    for connection in range(len(model.visited_connections[index])):
        model.visited_connections[index][connection].visit -= 1

    # substracting the duration of the specific traject (index) from the total time
    model.total_time -= model.time_dict[index]
    return model


def remove_traject(model, index):
    """
    Changing model parameters and emptying the traject that corresponds with the input index
    """

    # decreasing the number of trajects
    model.number_traject -= 1

    # change the model parameters corresponding to the removal of the traject
    model = change_model_parameters(model, index)

    # physical emptying the traject
    model.traject[index] = []

    return model


def replace_traject(model, index, type_base, type_hillclimber):
    """
    Replaces a single traject (index) with a randomly generated traject
    """

    # changing model parameters when running random hillclimber
    if type_hillclimber == 0:
        model = change_model_parameters(model, index)

    # randomly choosing a starting station
    station = random.choice(model.stations)

    # creating a randomly generated traject
    if type_base == 0:
        latest_traject, time, connections = make_baseline_traject(station)

    # creating a greedy generated traject (based on shortest distance between stations)
    if type_base == 1:
        latest_traject, time, connections = make_greedy_traject(station)

    # adapting model parameters to the newly added traject
    model.traject[index] = latest_traject
    model.total_time += time
    model.time_dict[index] = time
    model.visited_connections[index] = connections

    # changing number of trajects for worst traject hillclimber
    if type_hillclimber == 1:
        model.number_traject += 1

    return model


def get_worst_traject_index(best_version):
    """
    This function looks through the different trajects
    of the model. It removes them one by one, calculating each the quality score for each.
    The model is then being set back to the original state with every traject.
    The function returns the index of the traject that, when removed,
    still generated the highest quality score.
    This traject is seen as the least contributing or 'worst' traject of the model.
    """

    # creating list with scores of model without one traject
    changed_scores = []

    # looping over the trajects, saving the corresponding quality scores
    # of when the i'th traject is removed from the input model
    for i in range(len(best_version.traject)):
        copy_version = copy.deepcopy(best_version)

        # removing a traject and calculating the score of the model without the traject
        removed_version = remove_traject(copy_version, i)
        quality_score(removed_version)
        changed_scores.append(removed_version.score)

    # returning the index of the traject with corresponding highest quality score of the list
    max_index = np.argmax(changed_scores)
    return max_index


def execute_hillclimber(model, type_base, type_hillclimber):
    """
    Executing a hillclimber, dependent on the type of hillclimber the user likes
    """

    try:
        best_scores = []
        counter = 0

        # initializing a best version for the first run and
        # to change later on when a higer score is reached
        best_version = copy.deepcopy(model)

        # looping until KeyboardInterrupt
        while True:

            # creating a version to be changed of the current best version
            change_version = copy.deepcopy(best_version)

            # when the worst traject hillclimber is selected
            if type_hillclimber == 1:

                # getting the index of the perceived worst traject, removing this traject
                # and replacing this with a newly generated traject
                max_index = get_worst_traject_index(best_version)
                change_version = remove_traject(change_version, max_index)
                new_model = replace_traject(
                    change_version, max_index, type_base, type_hillclimber
                )

            # when the random hillclimber is selected
            elif type_hillclimber == 0:

                # choosing a random index that corresponds with the
                # traject that should be changed
                random_index = random.randint(0, len(model.traject) - 1)

                # replace the respective traject
                new_model = replace_traject(
                    change_version, random_index, type_base, type_hillclimber
                )

            # calculate quality score and compare with the best
            # possible score, if new score is better,
            # overwrite current best scoring model
            quality_score(new_model)
            if new_model.score >= best_version.score:
                best_version = new_model

            # print counter and score every 500 steps
            counter += 1
            if counter % 500 == 0:
                print(counter)
                print(
                    best_version.score,
                )

            # append best score to list to plot
            best_scores.append(best_version.score)

    # stop loop when the user executes a KeyboardInterrupt
    except KeyboardInterrupt:
        pass

    return best_version.traject, best_version.score, best_version.fraction, best_scores
