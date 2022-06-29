"""
=================================================
make_hist.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Creates a histogram based of the data it receives
=================================================
"""

import matplotlib.pyplot as plt
import csv


NUM_BINS = 20  # <- number of bins for the repeated base algorithm histogram


def make_hist():
    """
    Receives the base type, the key and the data and plots the data into a histogram
    """

    # histogram for when the repeated base algorithm is run
    hist_data_annealing = []
    with open("output/histo_data_annealing.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")

        counter = 0
        for row in csv_reader:
            if counter == 0:
                for score in row:
                    hist_data_annealing.append(float(score))
            counter += 1

    f.close()

    hist_data_hillclimber = []
    with open("output/histo_data_hillclimber.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")

        counter = 0
        for row in csv_reader:
            if counter == 0:
                for score in row:
                    hist_data_hillclimber.append(float(score))
            counter += 1

    f.close()

    hist_data_simple = []
    with open("output/histo_data.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")

        counter = 0
        for row in csv_reader:
            if counter == 0:
                for score in row:
                    hist_data_simple.append(float(score))
            counter += 1

    f.close()
    plt.hist(
        hist_data_hillclimber, NUM_BINS, alpha=0.5, label="Hillclimber"
    )
    plt.hist(
        hist_data_annealing,
        NUM_BINS,
        alpha=0.5,
        label="Simulated Annealing",
    )
    # plt.hist(hist_data_simple, NUM_BINS, alpha=0.5, label="Repeated Random")

    plt.title("Histogram Hillclimber and Simulated Annealing algorithms")
    plt.xlabel("Model quality score")
    plt.ylabel("Occurence of score")
    plt.legend()
    plt.savefig("output/histogram.png")


def make_plot(key):
    # plot for when the hillclimber or simmulated annealing are run
    # load data from csv file
    plot_data_annealing = []
    time_annealing = []
    with open("output/plot_data_annealing.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")

        counter = 0
        for row in csv_reader:
            if counter == 0:
                for score in row:
                    plot_data_annealing.append(float(score))
            else:
                for time_data in row:
                    time_annealing.append(float(time_data))
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

    plt.plot(time_hillclimber, plot_data_hillclimber, label="Hillclimber")
    plt.plot(time_annealing, plot_data_annealing, label="Simulated Annealing")

    plt.title("Hillclimber algorithm vs Simulated Annealing")

    plt.xlabel("Seconds")
    plt.ylabel("Model quality score")
    plt.legend()
    plt.grid()
    plt.rcParams["figure.dpi"] = 500
    plt.savefig("output/plot.png")
