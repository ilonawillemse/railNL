"""
=================================================
Code.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
=================================================
"""

import csv
import random

from matplotlib.pyplot import legend


class Station():
    "Station Object"
    def __init__(self, name, xcor, ycor):
        self.name = name
        self.connections = {}
        self.visited = 0
        self.xcor = xcor
        self.ycor = ycor
        

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = []
        self.score = 0
        self.quality = 0
        self.fraction = 0
        self.number_traject = random.randint(2,2)
        self.total_time = 0
    

    def fraction_visited(self):
        "calculated fraction of visited stations"
        visited_stations = 0
        for station in self.stations:
            if station.visited != 0:
                visited_stations += 1

        self.fraction = visited_stations / len(self.stations)

    def quality_score(self):
        "calculate quality score of model"
        self.fraction_visited()
        self.quality = self.fraction * 10000 - (self.number_traject * 100 + self.total_time)
        return self.quality

    
    def load_stations(self):
        "load the stations from database"
        with open(f"data_holland/StationsHolland.csv") as f:

            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            
            for row in csv_reader:
                name = row[0]
                xcor = row[1]
                ycor = row[2]
                self.stations.append(Station(name, xcor, ycor))
            
            f.close()


    def add_connections(self):
        "add the connections of the stations"

        with open(f"data_holland/ConnectiesHolland.csv") as f:

            csv_reader = csv.reader(f, delimiter = ',')
            next(csv_reader)

            all_lines = []
            for lines in csv_reader:
                all_lines.append(lines)

            for station in self.stations:
                for connection in all_lines:
                    station_name = connection[0]
                    connection_name = connection[1]
                    distance = connection[2]
                    if station.name == station_name:
                        
                        for i in range(len(self.stations)):
                            if connection_name == self.stations[i].name:
                                station.connections[self.stations[i]] = distance
                                self.stations[i].connections[station] = distance
                    

    def make_traject(self):
        self.traject = []
        time_dict = {}
        self.total_time = 0
        time = 0

        for i in range(self.number_traject):
            visited_stations = []
            station = random.choice(self.stations)
            visited_stations.append(station)
            station.visited += 1

            traject_length = random.randint(3,5)

            for _ in range(traject_length):
                connections = list(station.connections.items())

                new_choice = random.choice(connections)
                new_station = new_choice[0]
                new_distance = new_choice[1]


                counter = 0

                while new_station in visited_stations and counter < 100:
                    new_choice = random.choice(connections)
                    new_station = new_choice[0]
                    new_distance = new_choice[1]
                    counter += 1

                if counter == 100:
                    break

                time += int(new_distance)

                station = new_station
                visited_stations.append(station)
                station.visited += 1
            
            self.traject.append(visited_stations)  

            time_dict[f'train_{i+1}'] = int(time)
            self.total_time += time
            time = 0

        print(time_dict)
        # print(self.total_time)



    def get_name(self, list):
        for i in range(len(list)):
            list[i] = list[i].name
        return list


    def output_generate(self):
        with open('output.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['train', 'stations'])

            for i in range(len(self.traject)):
                self.traject[i] = self.get_name(self.traject[i])
                data = [f'train_{i+1}', self.traject[i]]
                writer.writerow(data)
            
            writer.writerow(['score', format(self.quality, '.3f')])


def visualization():
    from copy import deepcopy
    import plotly.graph_objects as go

    x_cor = []
    y_cor = []
    name = []
    connection_list = []

    for i in range(len(station.stations)):
        y_cor.append(float(station.stations[i].xcor))
        x_cor.append(float(station.stations[i].ycor))
        name.append(station.stations[i].name)

        connection_x_cor = []
        connection_y_cor = []

        current_station = station.stations[i]

        for connection in current_station.connections:
            connection_y_cor.append(float(current_station.xcor))
            connection_x_cor.append(float(current_station.ycor))
            connection_y_cor.append(float(connection.xcor))
            connection_x_cor.append(float(connection.ycor))
    
        connection = go.Scatter(x = connection_x_cor, y = connection_y_cor, line=dict(color="grey"))
        connection_list.append(connection)

    connection_list.append(go.Scatter(x = x_cor, y = y_cor, mode = "markers", hovertext= name, line=dict(color="lightgreen"),opacity= 0.6 ))


    # add train
    list_y_cor = []
    list_x_cor = []

    total_list_x_cor = []
    total_list_y_cor = []
    
    for i in range(len(station.traject)):
        counter = 0
        
        list_y_cor.clear()
        list_x_cor.clear()

        while counter < 30:
            for j in range(len(station.traject[i])):
                if counter == 30:
                    break

                list_y_cor.append(float(station.traject[i][j].xcor))
                list_x_cor.append(float(station.traject[i][j].ycor))
                counter += 1

            for k in range(len(station.traject[i])-2 , 0, -1):
                if counter == 30:
                    break

                list_y_cor.append(float(station.traject[i][k].xcor))
                list_x_cor.append(float(station.traject[i][k].ycor))
                counter += 1

        total_list_x_cor.append(deepcopy(list_x_cor))
        total_list_y_cor.append(deepcopy(list_y_cor))

    # print(total_list_x_cor)
    # print(total_list_y_cor)

    final_list_x_cor = []
    final_list_y_cor = []
    current_list = []

    for i in range(len(list_x_cor)):
        final_list_x_cor = [item[i] for item in total_list_x_cor]
        final_list_y_cor = [item[i] for item in total_list_y_cor]

        current = go.Frame(data=[go.Scatter(x = final_list_x_cor, y = final_list_y_cor, mode = "markers", line=dict(color="red") )], 
                            layout=go.Layout(title_text="No way, railway"))
        current_list.append(current)


    fig = go.Figure(
        data= connection_list,
        layout=go.Layout(
        xaxis=dict(range=[3.5, 6.5], autorange=False),
        yaxis=dict(range=[51, 54], autorange=False),
        title="No way, railway",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Let's rail",
                        method="animate",
                        args=[None])])]),
                        
    # add train 
    frames= current_list, 
    )

    # Add background image
    fig.add_layout_image(
            dict(
                source="https://cdn.pixabay.com/photo/2014/04/02/10/18/netherlands-303419_960_720.png",
                xref="x",
                yref="y",
                x=3.52,
                y=53.7,
                sizex=3.5,
                sizey=3.0,
                sizing="stretch",
                opacity=0.5,
                layer="below")
    )
    fig.update_layout(template="plotly_white", showlegend = False)

    fig.show()


if __name__ == "__main__":

    station = Model()

    station.load_stations()
    station.add_connections()
    station.make_traject()

    # visualization
    visualization()

    # for output csv
    station.quality_score()
    station.output_generate()





    # noteee: doe __repr__:
    #   def __repr__(self):
    #     return f"Station: {self.name} ({self.xcor})({self.ycor})"