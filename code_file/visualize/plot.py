"""
=================================================
make_hist.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Creates a histogram based of the data it receives
=================================================
"""

import matplotlib.pyplot as plt
import numpy as np


NUM_BINS = 100  # <- number of bins for the repeated base algorithm histogram


def make_hist(type_base, all_data, key):
    """
    Receives the base type, the key and the data and plots the data into a histogram
    """

    # histogram for when the repeated base algorithm is run
    data = all_data
    plt.hist(data, NUM_BINS)

    if key == 0:
        if type_base == 0:
            plt.title("Baseline algorithm: distribution of model data")

        elif type_base == 1:
            plt.title("Greedy algorithm: distribution of model data")

    if key == 1:
        plt.title("Hillclimber algorithm")

    if key == 2:
        plt.title("Simulated Annealing algorithm")

    plt.xlabel("Model quality score")
    plt.ylabel("Occurence of score")
    plt.savefig("output/histogram.png")


def make_plot(key, RUNNING_TIME, plot_data):
    # plot for when the hillclimber or simmulated annealing are run
    if key == 1 or key == 2:
        time = np.linspace(0, RUNNING_TIME, len(plot_data))

        plt.plot(time, plot_data)

        if key == 1:
            plt.title("Hillclimber algorithm: best scores over time")

        elif key == 2:
            plt.title("Simulated annealing algorithm: scores over time")

        plt.xlabel("Seconds")
        plt.ylabel("Model quality score")
        plt.savefig("output/plot.png")
