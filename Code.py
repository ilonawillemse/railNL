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
from algorithms.hillclimber import run_hillclimber
from algorithms.greedy import get_started
from algorithms.annealing import run_simulated_annealing
import pickle

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
    key = int(input("What would you like to run: baseline(0), greedy(1), hillclimber baseline(2), hillclimber greedy(3), simulated annealing baseline(4), simulated annealing greedy(5): "))

    # # ophalen van opgeslagen data
    # if key == 20:
    #     file = open("saved", "rb")
    #     print(pickle.load(file))

    if key == 0:
    # ---------------------------------baseline-------------------------------
        best_traject = []
        all_scores = []
        highest_score = 0
        with open('output/histo_data.csv', 'w') as output_file:
            try:
                i = 0
                while True:
                    model = Model()
                    model.baseline()
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
        visualization(model, best_traject)

    if key == 1:
    # ---------------------------------greedy-------------------------------
        # model = Model()
        # model.greedy()
     
        best_traject = []
        all_scores = []
        highest_score = 0
        with open('output/histo_data.csv', 'w') as output_file:
            try:
                i = 0
                while True:
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
                    # print(i)
                    i += 1
                    print(highest_score)
                    print(len(best_traject))
            except KeyboardInterrupt:
                pickle.dump(best_traject, open("saved", "wb"))
                pass
            
        output_generate(best_traject, highest_score, best_fraction)
        data = all_scores
        num_bins = 100 # <- number of bins for the histogram
        plt.hist(data, num_bins)
        plt.savefig("output/histogramgreedy.png")
        # visualization(model, best_traject)

    if key == 2:
    # -------------------------------hillclimber baseline------------------------------
        best_score = 0
        best_traject = []
        best_fraction = 0


        try:
            counter = 0
            while True:
                model = Model()
                model.baseline()
                traject, score, fraction = run_hillclimber(model, key)

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
        
        
        # model = Model()
        # model.baseline()

        # best_traject, best_score, best_fraction = run_hillclimber(model,key)

        output_generate(best_traject, best_score, best_fraction)
        # visualization(model, best_traject)




    if key == 3:
    # -------------------------------hillclimber greedy-------------------------------
        best_score = 0
        best_traject = []
        best_fraction = 0

        highest_score = 0
        model = Model()
        model.greedy()
        for i in range(1000):
            print(i)
            # writer = csv.writer(output_file) 
            if model.score < highest_score:
                model = Model()
                model.greedy()

        try:
            counter = 0
            while True:
                # model = Model()
                # model.greedy()
                traject, score, fraction = run_hillclimber(model, key)

                if score >= best_score:
                    best_traject = traject
                    best_score = score
                    best_fraction = fraction
                counter += 1
                # print(counter)
                print(best_score)
                print(len(best_traject))

        except KeyboardInterrupt:
            pickle.dump(best_traject, open("saved", "wb"))
            pass

        # model = Model()
        # model.greedy()

        # best_traject, best_score, best_fraction = run_hillclimber(model, key)

        # output_generate(best_traject, best_score, best_fraction)
        # visualization(model, best_traject)

    if key == 4:
    #-------------------------------simulated annealing----------------------------

        model = Model()
        model.baseline()

        best_traject, best_score, best_fraction = run_simulated_annealing(model, key)

        output_generate(best_traject, best_score, best_fraction)


    if key == 5:
    #-------------------------------simulated annealing----------------------------

        model = Model()
        model.greedy()

        best_traject, best_score, best_fraction = run_simulated_annealing(model, key)

        output_generate(best_traject, best_score, best_fraction)
