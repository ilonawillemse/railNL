"""""
DISCLAIMER: STILL BUGGED, DOES NOT KEEP TRACK OF THE TOTAL TIME OF THE MODEL PROPERLY SO THE SCORES IT GIVES ARE INCORRECT

Depth Hillclimber

- Removes a random traject and replaces it with a traject made using depth search
- The depth search starts with a random station station and then creates all possible valid trajects from that station
- Puts the best traject into the model, and saves this model if its better than the best model found so far
- Highly recommended to run with the Holland data instead of the National data due to runtime
- Print station_names in the depth function (see commented code) to see the algorithm go through all the possible trajects

"""""

from code_file.helpers import quality_score
import copy
import random

def remove_traject(model, index):
    """""
    Removes a traject from all of the trajects and changes the total time of the model accordingly
    """""
    
    time = model.time_dict[index]
    model.total_time -= time
    
    for connection in range(len(model.visited_connections[index])):
        model.visited_connections[index][connection].visit -= 1
    
    model.traject[index] = []
    
    return model

def depth_hillclimber(model):
    """""
    Runs the depth algorithm on a randomly created model and keeps track of the best model that is created
    """""
    best_version = copy.deepcopy(model)
    try:
        while True:
            change_version = copy.deepcopy(best_version)
            index = random.randint(0, len(model.traject) - 1)
            removed_version = remove_traject(change_version, index)
            new_model = depth(removed_version, index)


            if new_model.score >= best_version.score:
                best_version = copy.deepcopy(new_model)
            print(best_version.score, 'best')
            print(new_model.score, 'new')
    except:
        KeyboardInterrupt

    return best_version.traject, best_version.score, best_version.fraction

def depth(model, index):
    """""
    Depth search, goes through all possible trajects of a randomly chosen starting station and returns the best model
    """""

    stack = [[random.choice(model.stations)]]
    time_stack = [0]
    best_model = model
    print('Starting station:', stack[0][0].name)

    while len(stack) > 0:
        state = stack.pop()
        stack_time = time_stack.pop()

        # Goes through all the connections of the last station in the stack
        for connection in state[-1].connections.values():
            # Adds the time of the connection to the time of the traject
            time = stack_time
            time += int(float(connection.duration))
            child = copy.deepcopy(state)

            # Finds the next station
            if state[-1].name != connection.start.name:
                new_station = connection.start
            else:
                new_station = connection.end

            station_names = []
            for station in child:
                station_names.append(station.name)

            # Adding the next station would result in a valid traject, create a new child including this station and add it to the stack
            if new_station.name not in station_names and time <= 120:
                # Uncomment the following print statement to see the depth search
                # print(station.name)

                child.append(new_station)
                stack.append(child)
                time_stack.append(time)

                model.traject[index] = child
                model.total_time += time
                model.time_dict[index] = time

                # Turns the stations into pairs to be able to 'visit' their connections
                station_pairs = []
                for i in range(len(model.traject[index]) - 1):
                    station_pairs.append([model.traject[index][i], model.traject[index][i + 1]])

                # Visits the connections for score calculation purposes
                for connection in model.all_connections.values():
                    for station_pair in station_pairs:
                        if connection.start.name == station_pair[0].name and connection.end.name == station_pair[1].name:
                            connection.visit += 1
                        elif connection.end.name == station_pair[0].name and connection.start.name == station_pair[1].name:
                            connection.visit += 1

                quality_score(model)

                # Unvisit the connections
                for connection in model.all_connections.values():
                    for station_pair in station_pairs:
                        if connection.start.name == station_pair[0].name and connection.end.name == station_pair[1].name:
                            connection.visit -= 1
                        elif connection.end.name == station_pair[0].name and connection.start.name == station_pair[1].name:
                            connection.visit -= 1

                # Substracts the time of the traject from the model again
                model.total_time -= time
                model.time_dict[index] = 0

                if model.score >= best_model.score:
                    best_model = copy.deepcopy(model)

    return best_model

                