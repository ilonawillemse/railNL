# algorithms

```
In this map the different kinds of algorithms for 'solving' the railway problems can be found and a function to run the algorithms
```

A file that make the chosen algoritm run (run_algoritm.py)

Algorithms that can be found:
- baseline.py (a random algorithm with a bias of not being able to visit the same station in one traject twice)
- greedy.py (a greedy algorithm that looks for the shortest duration between stations and takes this as a base to find the stations for the traject)
- hillclimber.py (takes better and equal quality scores as answer and tries to find the optimum by doing so)
- annealing.py (takes the hillclimbeer as base but also accepts deteriorations with a certain chance. The acceptence of deteriorations declines the further in the run)