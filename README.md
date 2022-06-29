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
Make trainconnections of North and South Holland, max of 7 trajects within a timeframe of 2 hours. All rails must be used.

train,stations
train_1,"[Schiphol Airport, Amsterdam Zuid, Amsterdam Amstel, Amsterdam Centraal, Amsterdam Sloterdijk, Haarlem, Beverwijk, Zaandam, Castricum, Alkmaar, Hoorn]"
train_2,"[Rotterdam Centraal, Schiedam Centrum, Delft, Den Haag Centraal, Gouda, Alphen a/d Rijn, Leiden Centraal, Heemstede-Aerdenhout, Haarlem, Beverwijk, Castricum]"
train_3,"[Amsterdam Sloterdijk, Haarlem, Beverwijk, Castricum, Zaandam, Hoorn, Alkmaar, Den Helder]"
train_4,"[Dordrecht, Rotterdam Centraal, Rotterdam Alexander, Gouda, Den Haag Centraal, Leiden Centraal, Schiphol Airport, Amsterdam Zuid, Amsterdam Sloterdijk, Amsterdam Centraal, Amsterdam Amstel]"
train_5,"[Alphen a/d Rijn, Gouda, Den Haag Centraal, Leiden Centraal, Heemstede-Aerdenhout, Haarlem, Beverwijk, Castricum, Zaandam, Amsterdam Sloterdijk, Amsterdam Zuid]"
score,8864.0
fraction,1.000
```
![All rails used](............png)

### Assignment 2:
```
Make trainconnections of North and South Holland, max of 7 trajects within a timeframe of 2 hours. Try to get K as high as possible.

train,stations
train_1,"[Beverwijk, Zaandam, Castricum, Alkmaar, Den Helder]"
train_2,"[Haarlem, Amsterdam Sloterdijk, Amsterdam Zuid, Schiphol Airport, Leiden Centraal, Den Haag Centraal, Gouda, Rotterdam Alexander, Rotterdam Centraal, Dordrecht]"
train_3,"[Amsterdam Zuid, Amsterdam Amstel, Amsterdam Centraal, Amsterdam Sloterdijk, Zaandam, Hoorn, Alkmaar, Castricum, Beverwijk, Haarlem, Heemstede-Aerdenhout]"
train_4,"[Heemstede-Aerdenhout, Leiden Centraal, Alphen a/d Rijn, Gouda, Rotterdam Alexander, Rotterdam Centraal, Schiedam Centrum, Delft, Den Haag Centraal]"
score,9192.0
fraction,1.000
```
![Holland with high K value](............png)

### Assignment 3:
```
Make trainconnections of the Netherlands, max of 20 trajects within a timeframe of 3 hours. Try to get K as high as possible.

Zie hieronder de traject van de beste lijnvoering die we gevonden hebben. Alle connecties worden hierbij bereden behalve die van Sittard naar Heerlen. Een extra traject toevoegen alleen om deze connectie mee te nemen zou ook niet voor een verbetering in de score zorgen. Aangezien dit 1/89*10000 - 100 - 15 = -2.64 punten op zou leveren. Echter zijn er mogelijk nog wel andere samenstellingen van trajecten die voor een betere score zouden zorgen.  

train,stations
train_1,"Lelystad Centrum, Almere Centrum, Amsterdam Amstel, Amsterdam Centraal, Amsterdam Sloterdijk, Amsterdam Zuid, Schiphol Airport, Leiden Centraal, Den Haag Laan v NOI, Delft, Den Haag Centraal, Gouda, Den Haag HS"
train_2,"Enschede, Hengelo, Almelo, Deventer, Apeldoorn, Amersfoort, Utrecht Centraal, Hilversum, Amsterdam Amstel, Amsterdam Zuid, Schiphol Airport, Leiden Centraal, Den Haag Centraal"
train_3,"Almelo, Zwolle, Assen, Groningen, Leeuwarden, Heerenveen, Steenwijk"
train_4,"Venlo, Helmond, Eindhoven, s-Hertogenbosch, Oss, Nijmegen, Arnhem Centraal, Dieren, Zutphen, Deventer, Zwolle, Steenwijk"
train_5,"Maastricht, Sittard, Roermond, Weert, Eindhoven, Tilburg, Breda, Dordrecht, Rotterdam Blaak, Rotterdam Alexander, Rotterdam Centraal, Schiedam Centrum, Delft, Den Haag HS, Leiden Centraal"
train_6,"Den Helder, Alkmaar, Castricum, Beverwijk, Zaandam, Amsterdam Sloterdijk, Haarlem, Heemstede-Aerdenhout, Leiden Centraal, Alphen a/d Rijn, Gouda, Utrecht Centraal"
train_7,"Hilversum, Almere Centrum, Amsterdam Centraal, Amsterdam Amstel, Utrecht Centraal, s-Hertogenbosch, Tilburg, Breda, Etten-Leur, Roosendaal, Dordrecht"
train_8,"Alkmaar, Hoorn, Zaandam, Castricum, Beverwijk, Haarlem, Amsterdam Sloterdijk, Amsterdam Centraal, Utrecht Centraal, Schiphol Airport, Amsterdam Zuid"
train_9,"Alphen a/d Rijn, Utrecht Centraal, Ede-Wageningen, Arnhem Centraal, Dieren, Zutphen, Apeldoorn, Amersfoort, Zwolle"
train_10,"Den Haag Laan v NOI, Gouda, Rotterdam Alexander, Rotterdam Blaak, Schiedam Centrum, Rotterdam Centraal, Dordrecht, Roosendaal, Vlissingen"
score,7193.640449438202
fraction,0.989
```
![Netherlands with high K value](............png)


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
