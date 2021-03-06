"""
=================================================
helpers.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Some helper files to:
- return names for the output file
- generate an output file with the best trajects found
- calculates the fraction visited connections
- calculates the quality score
- keeps track of the best trajects and returns them

=================================================
"""

import csv


def get_name(list):
    """
    Takes the station objects and returns the names of the stations
    """

    names_list = []
    for i in range(len(list)):
        names_list.append(list[i].name)

    return names_list


def output_generate(traject, score):
    """
    Generates an output file with the trajects formed and corresponding quality score
    """

    with open("output/output_model.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["train", "stations"])
        for i in range(len(traject)):
            names = get_name(traject[i])
            separator = ", "
            x = separator.join(names)
            data = [f"train_{i+1}", x]
            writer.writerow(data)

        writer.writerow(["score", score])


def fraction_visited(model):
    """
    Calculates fraction of visited stations
    """

    visited_connections = 0
    for connection in model.all_connections:
        if model.all_connections[connection].visit != 0:
            visited_connections += 1

    model.fraction = visited_connections / len(model.all_connections)


def quality_score(model):
    """
    Calculates quality score of model
    """

    fraction_visited(model)
    model.score = model.fraction * 10000 - (
        model.number_traject * 100 + model.total_time
    )


def replace_best(score, traject, fraction):
    """
    Keeps track of the best trajects and returns the best
    """

    best_traject = traject
    best_score = score
    best_fraction = fraction

    return best_traject, best_score, best_fraction
