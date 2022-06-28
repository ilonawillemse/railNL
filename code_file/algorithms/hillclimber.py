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
import time


def change_model_parameters(model, index):
    """
    When removing a traject, this function changes some of the parameters
    (visitedness of connections and total time of the model) of
    the model to be able to add a new traject without taking on
    the old values of the parameters
    """

    # looping over every connection of the specific traject
    # (defined by the index) and decreasing the visitedness by one
    for connection in range(len(model.visited_connections[index])):
        model.visited_connections[index][connection].visit -= 1

    # decreasing the total time of the model by duration of
    # the old traject
    model.total_time -= model.time_dict[index]
    return model


def remove_traject(model, index):
    """
    ]Changing model parameters and emptying
     the traject that corresponds with the input index
    """

    # decreasing the number of trajects
    model.number_traject -= 1

    # decreasing the amount of visits of each connection with one
    # and decreasing the total time with the traject time of the
    # corresponding index
    model = change_model_parameters(model, index)

    # physical emptying the traject
    model.traject[index] = []

    return model


def replace_traject(model, index, type_base, type_hillclimber):
    """
    Replaces a single traject (corresponding with a given index)
    with a randomly generated one, for both random hillclimber and hillclimber
    that replaces the 'worst' traject.
    """

    # Running random hillclimber
    if type_hillclimber == 0:

        # decreasing the amount of visits of each connection with one
        # and decreasing the total time with the traject time of the
        # corresponding index
        model = change_model_parameters(model, index)

    # randomly choosing a starting station
    station = random.choice(model.stations)

    # creating a baseline (randomly generated) traject
    if type_base == 0:
        latest_traject, time, connections = make_baseline_traject(station)

    # creating a greedy (based on shortest distance
    # between stations) trajects
    if type_base == 1:
        latest_traject, time, connections = make_greedy_traject(station)

    # adapting model parameters to the newly added traject, thus
    # changing the time and the visitedness of connections
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
    of the model. It removes them one by one, setting the
    model back to its original state when the score of the
    model without a traject is saved. It returns the index of
    the traject without which the model score is the highest.
    This traject is seen as the least contributing or 'worst'
    traject of the model.
    """

    # creating list with scores of model without one traject
    changed_scores = []

    # looping over every traject in the model
    for i in range(len(best_version.traject)):

        # making a copy of the input model
        copy_version = copy.deepcopy(best_version)

        # removing a traject and calculating the score of
        # the model without the traject
        removed_version = remove_traject(copy_version, i)
        quality_score(removed_version)

        # appending the scores to a list
        changed_scores.append(removed_version.score)

    # finding the highest score of the list and
    # returning this score
    max_index = np.argmax(changed_scores)
    return max_index


def execute_hillclimber(model, type_base, type_hillclimber):
    """
    Executing a hillclimber, dependant on
    the input it gets, thus which type of hillclimber is
    specified.
    """

    time_list = []
    start = time.time()
    # initializing an empty list with the best scores to
    # plot the hillclimber
    best_scores = []

    # initializing a counter to print at 500 step
    # intervals, to keep track of the score
    counter = 0

    # initializing a best version for the first run and
    # to change later on when a higer score is reached
    best_version = copy.deepcopy(model)
    
    while time.time() - start < 10:
    # looping until KeyboardInterrupt

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
        current_time = time.time() - start
        #print(current_time)
        time_list.append(current_time)
    print(time_list)

    return best_version.traject, best_version.score, best_version.fraction, best_scores, time_list
