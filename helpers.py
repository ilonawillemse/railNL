
import csv

import matplotlib.pyplot as plt



def get_name(list):
    names_list = []
    for i in range(len(list)):
        names_list.append(list[i].name)
    return names_list

def output_generate(traject, score, fraction):
    with open('output/output_model.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['train', 'stations'])
        for i in range(len(traject)):
            names = get_name(traject[i])
            data = [f'train_{i+1}', names]
            writer.writerow(data)
        
        writer.writerow(['score', format(score, '.3f')])
        writer.writerow(['fraction', format(fraction, '.3f')])

def fraction_visited(model):
        "calculated fraction of visited stations"
        
        visited_connections = 0
        for connection in model.all_connections:
            if model.all_connections[connection].visit != 0:
                visited_connections += 1
        
        model.fraction = visited_connections / len(model.all_connections)
        

def quality_score(model):
    "calculate quality score of model"
    fraction_visited(model)
    model.score = model.fraction * 10000 - (model.number_traject * 100 + model.total_time)
    # print(model.number_traject)
    


           