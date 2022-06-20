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
from code_file.visualize import visualization
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
    key = int(input("What would you like to run: simple run(0), with hillclimber(1), simulated annealing(2): "))
    if key == 1:    
        hillclimber = int(input("random hillclimber(0) or regular hillclimber(1): "))
    
    choice = int(input("random(0) or greedy(1): "))
    vis = int(input("Would you like to visualize: no(0), yes(1): "))

    # ophalen van opgeslagen data
    if key == 20:
        file = open("saved", "rb")
        print(pickle.load(file))
    
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
                    # print(i)
                    print(highest_score)
                    print(len(best_traject))
                    i += 1
            except KeyboardInterrupt:
                pickle.dump(best_traject, open("saved", "wb"))
                pass
            
        output_generate(best_traject, highest_score, best_fraction)
        data = all_scores
        num_bins = 100 # <- number of bins for the histogram
        plt.hist(data, num_bins)
        plt.savefig("output/histogramtest.png")
        if vis == 1:
            visualization(model, best_traject)

    
    if key == 1:
    # --------------------hillclimber------------------------------
        best_score = 0
        best_traject = []
        best_fraction = 0

        try:
            counter = 0

            if hillclimber == 1:
                while True:
                    model = Model()
                    if choice == 0:
                        model.baseline()
                    if choice == 1:
                        model.greedy()

                    traject, score, fraction = run_hillclimber(model, choice)

                    if score >= best_score:
                        best_traject = traject
                        best_score = score
                        best_fraction = fraction
                    counter += 1
                    print(counter)
                    print(best_score)
                    print(len(best_traject))

        except KeyboardInterrupt:
            pickle.dump(best_traject, open("saved", "wb"))
            pass
        
        if hillclimber == 0:
            model = Model()
            if choice == 0:
                model.baseline()
            if choice == 1:
                model.greedy()
            best_traject, best_score, best_fraction, data = random_hillclimber(model, choice)

        output_generate(best_traject, best_score, best_fraction)
            
        if vis == 1:
            visualization(model, best_traject)
            plt.plot(data)
            plt.savefig("output/histogramtest.png")
        


    if key == 2:
    #-------------------------------simulated annealing----------------------------
        model = Model()
        if choice == 0:
            model.baseline()
        if choice == 1:
            model.greedy()

        best_traject, best_score, best_fraction = run_simulated_annealing(model, choice)

        output_generate(best_traject, best_score, best_fraction)
        if vis == 1:
            visualization(model, best_traject)
