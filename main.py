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
from code_file.helpers import output_generate, quality_score, replace_best
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

    best_score = 0
    counter = 0
    best_fraction = 0
    best_traject = [] 
    all_data = []

    key = int(input("What would you like to run: simple run(0), with hillclimber(1), simulated annealing(2): "))
    hillclimber = None
    if key == 1:    
        hillclimber = int(input("random hillclimber(0) or regular hillclimber(1): "))
    
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
        with open('output/histo_data.csv', 'w') as output_file:
            try:
                i = 0
                while True:
                    model = Model()
                    if choice == 0:
                        model.baseline()
                    if choice == 1:
                        model.greedy()
                    writer = csv.writer(output_file) 
                    if model.score > best_score:
                        best_traject, best_score, best_fraction = replace_best(model.score, model.traject, model.fraction)
                    score = model.score
                    all_data.append(score)
                    writer.writerow([score])
                    # print(i)
                    print(best_score)
                    print(len(best_traject))
                    i += 1
            except KeyboardInterrupt:
                pickle.dump(best_traject, open("saved", "wb"))
                pass
            
        output_generate(best_traject, best_score, best_fraction)
        data = all_data
        num_bins = 100 # <- number of bins for the histogram
        plt.hist(data, num_bins)
        if choice == 0:
            plt.title("Baseline algorithm: distribution of model data")
        elif choice == 1:
            plt.title("Greedy algorithm: distribution of model data")
        plt.xlabel("Model quality score")
        plt.ylabel("Occurence of score")
        plt.savefig("output/histogramtest.png")

    
    if key == 1 or key == 2:
    # --------------------hillclimber or simulated annealing------------------------------
        

        model = Model()
        if choice == 0:
            model.baseline()
        if choice == 1:
            model.greedy()

        if key == 1:
            best_traject, best_score, best_fraction, all_data = run_hillclimber(model, choice, hillclimber)
        if key == 2:
            try:
                while True:
                    traject, score, fraction, data = run_simulated_annealing(model, choice)
                    if score > best_score:
                        best_traject, best_score, best_fraction = replace_best(score, traject, fraction)
                    print(counter)
                    print(best_score)
                    all_data.extend(data)
                    counter += 1
            except:
                KeyboardInterrupt
                    
        output_generate(best_traject, best_score, best_fraction)
            
    
        plt.plot(all_data)
        if key == 1:
            plt.title("Hillclimber algorithm: best scores over time")
        elif key == 2:
            plt.title("Simulated annealing algorithm: scores over time")
        plt.xlabel("Number of iterations")
        plt.ylabel("Model quality score")
        plt.savefig("output/histogramtest.png")
        
