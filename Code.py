"""
=================================================
Code.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
=================================================
"""

import csv
import copy
import matplotlib.pyplot as plt
from helpers import output_generate, quality_score
from visualize import visualization
from loader import load_stations, add_connections
from algorithms.baseline import starting_trajects
from algorithms.hillclimber import run_hillclimber
from algorithms.greedy import get_started

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = load_stations()
        self.all_connections = add_connections(self.stations)
        self.visited_connections = []
        self.traject = []
        self.time_dict = {}
        self.score = 0
        self.fraction = 0
        self.number_traject = 0
        self.total_time = 0

    def baseline(self):
        starting_trajects(self)
        quality_score(self)  
    
    def greedy(self):
        get_started(self)
        quality_score(self) 


if __name__ == "__main__":

# # ---------------------------------baseline-------------------------------
#     best_traject = []
#     all_scores = []
#     highest_score = 0
#     with open('output/histo_data.csv', 'w') as output_file:
#         for i in range(100):
#             model = Model()
#             model.baseline()
#             writer = csv.writer(output_file) 
#             if model.score > highest_score:
#                 best_traject = model.traject
#                 highest_score = model.score
#                 best_fraction = model.fraction
#             score = model.score
#             all_scores.append(score)
#             writer.writerow([score])
#             print(i)
#     output_generate(best_traject, highest_score, best_fraction)
#     data = all_scores
#     num_bins = 100 # <- number of bins for the histogram
#     plt.hist(data, num_bins)
#     plt.savefig("output/histogramtest.png")
#     visualization(model, best_traject)


# # # ---------------------------------greedy-------------------------------
#     # model = Model()
#     # model.greedy()
#     # 
#     best_traject = []
#     all_scores = []
#     highest_score = 0
#     with open('output/histo_data.csv', 'w') as output_file:
#         for i in range(100):
#             model = Model()
#             model.greedy()
#             writer = csv.writer(output_file) 
#             if model.score > highest_score:
#                 best_traject = model.traject
#                 highest_score = model.score
#                 best_fraction = model.fraction
#             score = model.score
#             all_scores.append(score)
#             writer.writerow([score])
#             print(i)
#     output_generate(best_traject, highest_score, best_fraction)
#     data = all_scores
#     num_bins = 100 # <- number of bins for the histogram
#     plt.hist(data, num_bins)
#     plt.savefig("output/histogramgreedy.png")
#     # visualization(model, best_traject)


# # -------------------------------hillclimber baseline------mind: change import in hillclimber.p-------------------------
    model = Model()
    model.baseline()

    best_traject, best_score, best_fraction = run_hillclimber(model)

    # output_generate(best_traject, best_score, best_fraction)
    # visualization(model, best_traject)



## -------------------------------hillclimber greedy-----mind: change import in hillclimber.py--------------------------
    # model = Model()
    # model.greedy()

    # best_traject, best_score, best_fraction = run_hillclimber(model)

    # output_generate(best_traject, best_score, best_fraction)
    # visualization(model, best_traject)
