"""
=================================================
main.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
made interactive for user, based on with what algorithm they would like to run
=================================================
"""

import csv
import matplotlib.pyplot as plt
from code_file.helpers import output_generate, quality_score, replace_best
from code_file.loader import load_stations, add_connections
from code_file.algorithms.baseline import starting_trajects
from code_file.algorithms.hillclimber import run_hillclimber
from code_file.algorithms.greedy import get_started
from code_file.algorithms.annealing import run_simulated_annealing
from code_file.visualize_output import visualization_output


class Model:
    "Railway Model"

    def __init__(self):
        self.stations = load_stations()
        self.all_connections = add_connections(self.stations)
        self.visited_connections = []
        self.traject = []
        self.time_dict = {}
        self.score, self.fraction, self.number_traject, self.total_time = 0, 0, 0, 0

    def baseline(self):
        starting_trajects(self)
        quality_score(self)

    def greedy(self):
        get_started(self)
        quality_score(self)


if __name__ == "__main__":
    # dataclass ?-------------------
    best_score, counter, best_fraction, best_traject = 0, 0, 0, 0
    best_traject, all_data = [], []
    type_hillclimber = None

    key = int(
        input(
            "What would you like to run: simple run(0), with hillclimber(1), \
                simulated annealing(2), simulate output file(3): "
        )
    )

    if key == 1:
        type_hillclimber = int(input("random(0) or worst traject removal(1): "))

    if key != 3:
        type_base = int(input("random(0) or greedy(1): "))

    if key == 3:
        visualization_output(Model())

    # ---------------------run without hillclimber---------------------
    if key == 0:
        with open("output/histo_data.csv", "w") as output_file:
            try:
                while True:
                    model = Model()

                    if type_base == 0:
                        model.baseline()

                    if type_base == 1:
                        model.greedy()

                    writer = csv.writer(output_file)

                    if model.score > best_score:
                        best_traject, best_score, best_fraction = replace_best(
                            model.score, model.traject, model.fraction
                        )

                    score = model.score
                    all_data.append(score)
                    writer.writerow([score])
                    print(best_score)
                    print(len(best_traject))

            except KeyboardInterrupt:
                pass

        output_generate(best_traject, best_score, best_fraction)

        # make histogram
        data = all_data
        num_bins = 100  # <- number of bins for the histogram
        plt.hist(data, num_bins)

        if type_base == 0:
            plt.title("Baseline algorithm: distribution of model data")

        elif type_base == 1:
            plt.title("Greedy algorithm: distribution of model data")

        plt.xlabel("Model quality score")
        plt.ylabel("Occurence of score")
        plt.savefig("output/histogramtest.png")

    # --------------------hillclimber or simulated annealing------------------------------
    if key == 1 or key == 2:
        model = Model()
        if type_base == 0:
            model.baseline()
        if type_base == 1:
            model.greedy()

        # hillclimber
        if key == 1:
            best_traject, best_score, best_fraction, all_data = run_hillclimber(
                model, type_base, type_hillclimber
            )

        # simulated annealing
        if key == 2:
            try:
                while True:
                    traject, score, fraction, data = run_simulated_annealing(
                        model, type_base
                    )
                    if score > best_score:
                        best_traject, best_score, best_fraction = replace_best(
                            score, traject, fraction
                        )
                    # print(counter)
                    # print(best_score)
                    all_data.extend(data)
                    counter += 1

            except KeyboardInterrupt:
                pass

        output_generate(best_traject, best_score, best_fraction)

        # make histogram
        plt.plot(all_data)

        if key == 1:
            plt.title("Hillclimber algorithm: best scores over time")

        elif key == 2:
            plt.title("Simulated annealing algorithm: scores over time")

        plt.xlabel("Number of iterations")
        plt.ylabel("Model quality score")
        plt.savefig("output/histogramtest.png")
