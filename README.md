# RailNL
railNL programmeertheorie

# Project
```
With this programm an algoritm using heuristics is written in which the best railnetwork is being searched for both North/South Holland and the Netherlands. Run the program to find the best (highest) objective score for this problem.

Objective score can be calculated by:
K = p * 10000 - (T * 100 + Min)

in which the K is the objective score (quality score), T the number of trajects, Min the total duration and p the fraction of used connections.
```

# Usage:
```
Run "main.py" to enter the program and choose what algorithm you would like to run by following the instructions.
```


### Assignment 1:
```
make trainconnections of North and South Holland, max of 7 trajects within a timeframe of 2 hours. All rails must be used.
```
![All rails used](............png)

### Assignment 2:
```
make trainconnections of North and South Holland, max of 7 trajects within a timeframe of 2 hours. Try to get K as high as possible.
```
![Holland with high K value](............png)

### Assignment 3:
```
make trainconnections of the Netherlands, max of 20 trajects within a timeframe of 3 hours. Try to get K as high as possible.
```
![Netherlands with high K value](............png)

### Assignment 4:
```
Make a visualization of the results
```
![visualization](/doc/railnl.gif)

### Assignment 5:
```
Change 3 connections and look at the scores
```
![Change connections](............gif)

### Assignment 6:
```
Delete all Utrecht Centraal connections
```
![Remove Utrecht Centraal connections](............gif)

### Assignment 7:
```
Removal other stations and its impact
```
![Removal station](............gif)


# Experiment
```
We experimented with the maximum temperature for the simulated annealing.
By increasing this temperature the acceptance chance for worse quality scores is increased.
By testing different maximum temperatures we are able to find out what could be the best maximum temperature for running the simulated annealing with.

- NOTE: To change the maximum temperature you must follow the instructions when running the programm and enter the desired temperature:
    - "Would you like to choose the Max temp yourself? no(0), yes(1)?: "
    - "What would you like to be the max temperature for the simulated annealing: "

As you can see in the picture below, the spike amplitude increases with increased max temperature.
The corresponding best scores first increased when increasing the max temperature from 15 to 20 and 25.
After the max temperature of 25 the best scores did seem to look stable.
With the max temperature of 35 or higher the spike amplitude got so big it seemed kind off useless to spike so much.
The best score did not end up higher as well.
This is why we think the optimum maximum temperature should lay between 25 and 35.
Therefore, we chose our base max temperature to be 30.
```
![Experiment](/doc/experiment.png)


# Authors:
- Wesley Korff (12626465)
- Anouk Van Valkengoed (12379832)
- Ilona Willemse (11596120)

# License:
```
MIT License - see the LICENSE file for details
```
