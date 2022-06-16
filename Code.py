"""
=================================================
Code.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
=================================================
"""

import csv
import matplotlib.pyplot as plt
from helpers import output_generate, quality_score
from visualize import visualization
from loader import load_stations, add_connections
from algorithms.baseline import starting_trajects
from algorithms.greedy import get_started

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = load_stations()
        self.score = 0
        self.fraction = 0
        self.number_traject = 0
        self.total_time = 0
        self.traject = []
        self.time_dict = {}
        self.all_connections = add_connections(self.stations)

    def set_visited(self):
        for station in self.stations:
            station.visited = 0

        for station in self.stations:
            for traject in self.traject:
                if station in traject:
                    station.visited += 1       

    def baseline(self):
        starting_trajects(self)
        self.set_visited()
        quality_score(self) 
    
    def greedy(self):
        get_started(self)
        self.set_visited()
        quality_score(self) 


if __name__ == "__main__":
# ---------------greedy-----------
    # model = Model()
    # model.greedy()
    # output_generate(model.traject, model.score, model.fraction)
    # visualization(model, model.traject)

    best_traject = []
    all_scores = []
    highest_score = 0
    with open('output/histo_data.csv', 'w') as output_file:
        for i in range(10000):
            model = Model()
            model.greedy()
            writer = csv.writer(output_file) 
            if model.score > highest_score:
                best_traject = model.traject
                highest_score = model.score
                best_fraction = model.fraction
            score = model.score
            all_scores.append(score)
            writer.writerow([score])
            print(i)
    output_generate(best_traject, highest_score, best_fraction)
    data = all_scores
    num_bins = 100 # <- number of bins for the histogram
    plt.hist(data, num_bins)
    plt.savefig("output/histogramtestwithlimitreturning.png")
    visualization(model, best_traject)


# ---------------random-----------
    # model = Model()
    # model.baseline()

    # best_traject = []
    # all_scores = []
    # highest_score = 0
    # with open('output/histo_data.csv', 'w') as output_file:
    #     for i in range(10):
    #         model = Model()
    #         model.run()
    #         writer = csv.writer(output_file) 
    #         if model.score > highest_score:
    #             best_traject = model.traject
    #             highest_score = model.score
    #             best_fraction = model.fraction
    #         score = model.score
    #         all_scores.append(score)
    #         writer.writerow([score])
    #         print(i)
    # output_generate(best_traject, highest_score, best_fraction)
    # data = all_scores
    # num_bins = 100 # <- number of bins for the histogram
    # plt.hist(data, num_bins)
    # plt.savefig("output/histogramtest.png")
    # visualization(model, best_traject)
    
