# algorithms

```
In this map the different kinds of algorithms for 'solving' the railway problems can be found and a function to run the algorithms
```

A file that make the chosen algoritm run (run_algoritm.py)

Algorithms that can be found:
- baseline.py (a random algorithm with a bias of not being able to visit the same station in one traject twice)
    - The number of trajects is chosen randomly from 1 till 20 trajects. For plotting the data we suggest to chose a fixed number of trajects to compare the algorithms. You could change the number of trajects by uncomment the random generation and setting a fixed number of trajects.
- greedy.py (a greedy algorithm that looks for the shortest duration between stations and takes this as a base to find the stations for the traject)
- hillclimber.py (takes better and equal quality scores as answer and tries to find the optimum by doing so)
- annealing.py (takes the hillclimbeer as base but also accepts deteriorations with a certain chance. The acceptence of deteriorations declines the further in the run)
- depth_hillclimber.py (a hillclimber algorithm that searches depth first for the best trajects. DISCLAIMER: STILL BUGGED, DOES NOT KEEP TRACK OF THE TOTAL TIME OF THE MODEL PROPERLY SO THE SCORES IT GIVES ARE INCORRECT)
