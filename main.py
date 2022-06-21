"""
=================================================
main.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
made interactive for used based on what algorithm they would like to run the programm
=================================================
"""

import csv
import matplotlib.pyplot as plt
from code_file.helpers import output_generate, quality_score
from code_file.loader import load_stations, add_connections
from code_file.algorithms.baseline import starting_trajects
from code_file.algorithms.hillclimber import run_hillclimber
from code_file.algorithms.random_hillclimber import random_hillclimber
from code_file.algorithms.greedy import get_started
from code_file.algorithms.annealing import run_simulated_annealing
import pickle
from code_file.visualize_output import visualization_output



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
    key = int(input("What would you like to run: simple run(0), with hillclimber(1), simulated annealing(2), visualize(30): "))
    hillclimber = None
    if key == 1:    
        hillclimber = int(input("random hillclimber(0) or regular hillclimber(1): "))
    
    if key != 30:
        choice = int(input("random(0) or greedy(1): "))

    # ophalen van opgeslagen data
    if key == 20:
        file = open("saved", "rb")
        print(pickle.load(file))
    
    # visualize the output file
    if key == 30:
        visualization_output(Model())


    if key == 0:
    # ---------------------run without hillclimber---------------------
        best_traject = []
        all_scores = []
        highest_score = 0
        with open('output/histo_data.csv', 'w') as output_file:
            try:
                i = 0
                while True:
                    i += 1
                    model = Model()
                    if choice == 0:
                        model.baseline()
                    if choice == 1:
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
                    print(highest_score)
            except KeyboardInterrupt:
                pickle.dump(best_traject, open("saved", "wb"))
                pass
        
        output_generate(best_traject, highest_score, best_fraction)
        data = all_scores
        num_bins = 100 # <- number of bins for the histogram
        plt.hist(data, num_bins)
        plt.savefig("output/histogramtest.png")

    
    if key == 1 or key == 2:
    # --------------------hillclimber or simulated annealing------------------------------
        best_score = 0
        best_traject = []
        best_fraction = 0


        model = Model()
        if choice == 0:
            model.baseline()
        if choice == 1:
            model.greedy()

        if key == 1:
            if hillclimber == 0:
                best_traject, best_score, best_fraction, data = random_hillclimber(model, choice)
            if hillclimber == 1:
                best_traject, best_score, best_fraction, data= run_hillclimber(model, choice)

        if key == 2:
            traject, score, fraction = run_simulated_annealing(model, choice)
                    
        output_generate(best_traject, best_score, best_fraction)
            
        plt.plot(data)
        plt.savefig("output/histogramtest.png")
        
