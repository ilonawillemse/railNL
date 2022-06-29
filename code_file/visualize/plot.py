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
import csv


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


def make_plot(key):
    # plot for when the hillclimber or simmulated annealing are run
    # load data from csv file
    plot_data = []
    time = []
    with open("output/plot_data_annealing.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")

        counter = 0
        for row in csv_reader:
            if counter == 0:
                for score in row:
                    plot_data.append(float(score))
            else:
                for time_data in row:
                    time.append(float(time_data))
            counter += 1

    f.close()

    plot_data_hillclimber = []
    time_hillclimber = []
    with open("output/plot_data_hillclimber.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")

        counter = 0
        for row in csv_reader:
            if counter == 0:
                for score in row:
                    plot_data_hillclimber.append(float(score))
            else:
                for time_data in row:
                    time_hillclimber.append(float(time_data))
            counter += 1

    f.close()

    plt.plot(time_hillclimber, plot_data_hillclimber)
    plt.plot(time, plot_data)

    plt.title("Hillclimber algorithm vs Simulated Annealing")

    plt.xlabel("Seconds")
    plt.ylabel("Model quality score")
    # plt.legend()
    plt.savefig("output/plot.png")
