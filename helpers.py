
import csv

import matplotlib.pyplot as plt



def get_name(list):
    names_list = []
    for i in range(len(list)):
        names_list.append(list[i].name)
    return names_list

def output_generate(traject, score):
    with open('output.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['train', 'stations'])
        for i in range(len(traject)):
            names = get_name(traject[i])
            data = [f'train_{i+1}', names]
            writer.writerow(data)
        
        writer.writerow(['score', format(score, '.3f')])

def multiple_runs():
    all_scores = []
    highest_score = 0
    with open('histo_data.csv', 'w') as output_file:
        for i in range(10):
            model = Model()
            model.load_stations()
            model.add_connections()
            model.run()
            writer = csv.writer(output_file) 
            if model.score > highest_score:
                best_traject = model.traject
                highest_score = model.score
            score = model.score
            all_scores.append(score)
            writer.writerow([score])
            print(i)
            
    output_generate(best_traject, highest_score)

    # with open('best_traject_output.csv', 'w') as output_best_file:
    #         writer = csv.writer(output_best_file)
    #         writer.writerow(['train', 'stations'])

    #         for i in range(len(best_traject)):
    #             names = get_name(best_traject[i])
    #             data = [f'train_{i+1}', names]
    #             writer.writerow(data)
                            
    #         writer.writerow(['score', format(highest_score, '.3f')])
    
    data = all_scores
    num_bins = 100 # <- number of bins for the histogram
    plt.hist(data, num_bins)
    plt.savefig("histogramtest.png")