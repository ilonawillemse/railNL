"""
=================================================
visualize_output.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Visualizes the best traject combinations found in a plotly simulation by using the output file
All stations and connections are visualised with corresponding dots and lines
The trajects are visualised with colored lines, another color for each traject
Moving trains are visualised with the same color as the traject they are riding just for the fun effect
=================================================
"""

import plotly.graph_objects as go
import csv


def visualization_output(model):
    "visualize the trajects with trains riding them"
    
    # add the stations to the visualization
    stations_dict = {}
    name = []
    x_cor = []
    y_cor = []
    
    for station in model.stations:
        stations_dict[station.name] = station
        name.append(station.name)
        x_cor.append(station.ycor)
        y_cor.append(station.xcor)

    # add the connection lines to the visualization
    connection_list = []

    for _, value in model.all_connections.items():
        connection_x_cor = []
        connection_y_cor = []
        connection_list.append(go.Scatter(x = x_cor, y = y_cor, 
                                mode = "markers", 
                                hovertext= name, 
                                opacity= 1 ))

        connection_x_cor.append(float(value.start.ycor))
        connection_y_cor.append(float(value.start.xcor))
        connection_y_cor.append(float(value.end.xcor))
        connection_x_cor.append(float(value.end.ycor))

        connection = go.Scatter(x = connection_x_cor, y = connection_y_cor, 
                                        mode = "markers + lines",
                                        line = dict(color="grey", dash = "dot"),
                                        opacity = 1)
        connection_list.append(connection)

    # add station dots
    connection_list.append(go.Scatter(x = x_cor, y = y_cor, 
                            mode = "markers", 
                            hovertext = name,
                            marker = dict(color = "grey"),
                            opacity = 1 ))

    # extra adding the first connection at the beginning of the list so that this dot stays visible too
    connection_list.insert(0, connection)
    

# ------------------------------------------moving trains---------------------------------------------
    # read the trajects from csv file and get the corresponding station objects to obtain the information about the stations
    traject_names = []
    with open(f"best_nationaal.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            traject_row = []
            tmp = row[1].split(', ')
            for i in range(len(tmp)):
                traject_row.append(tmp[i])
            traject_names.append(traject_row)
        traject_names.pop()
        f.close()

    # compare the station names with the stations and exchange them for the Station() objects
    traject_objects = []
    for traject in traject_names:
        trajects = []
        for station in traject:
            trajects.append(stations_dict.get(station))
        traject_objects.append(trajects)

    all_traject_x_cor = []
    all_traject_y_cor = []
    
    # make the train move back and forth
    for i in range(len(traject_objects)):
        number_of_moves = 0
        traject_y_cor = []
        traject_x_cor = []
       
        while number_of_moves < 100:
            # make the trains move across the traject
            for j in range(len(traject_objects[i])):
                if number_of_moves == 100:
                    break
                
                # x and y coordinates were switched in the csv file
                traject_y_cor.append(float(traject_objects[i][j].xcor))
                traject_x_cor.append(float(traject_objects[i][j].ycor))
                number_of_moves += 1

            # make the trains move back across the traject when they reach the end
            for k in range(len(traject_objects[i])-2 , 0, -1):
                if number_of_moves == 100:
                    break

                # x and y coordinates were switched in the csv file
                traject_y_cor.append(float(traject_objects[i][k].xcor))
                traject_x_cor.append(float(traject_objects[i][k].ycor))
                number_of_moves += 1
        
        # create a list of lists with coordinates of the train trajects
        all_traject_x_cor.append(traject_x_cor)
        all_traject_y_cor.append(traject_y_cor)

        # add traject lines with different colors for every traject
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'blueviolet', 'pink']
        colors = colors + colors + colors
        

        connection_list.append(go.Scatter(x = traject_x_cor, y = traject_y_cor, 
                                mode = "lines", 
                                line = dict(color = colors[i]),
                                opacity = 1 ))


    # making the trains of different trajects ride together by comprehending the first coordinates of every traject
    # add train name
    traject_number = []
    for i in range(len(traject_objects)):
        traject_number.append(f"train {i + 1}")

    list_x_cor = []
    list_y_cor = []
    current_stations = []

    for i in range(len(traject_x_cor)):
        list_x_cor = [item[i] for item in all_traject_x_cor]
        list_y_cor = [item[i] for item in all_traject_y_cor]

        current = go.Frame(data = [go.Scatter(
                            x = list_x_cor, 
                            y = list_y_cor, 
                            mode = "markers", 
                            hovertext = traject_number,
                            marker = dict(color = colors, size = 13),
                            opacity = 1)], 
                            layout = go.Layout(title_text = "No way, railway"))


        current_stations.append(current)

    # create the figure with connections/ stations and trains
    fig = go.Figure(
        data = connection_list,
        layout = go.Layout(
        xaxis = dict(range = [1, 10], autorange=False),
        yaxis = dict(range = [50.5, 54], autorange=False),
        title = "No way, railway",
        showlegend = False,
        template = "plotly_white",
        updatemenus = [dict(
            type = "buttons",
            buttons = [dict(label = "Let's rail",
                        method = "animate",
                        args = [None, 
                            {'frame': { "duration": 1000, "redraw": True},}
                            ])])]),
                        
    # add moving trains
    frames = current_stations
    )

    # Add background image
    fig.add_layout_image(dict(
                source = "https://cdn.pixabay.com/photo/2014/04/02/10/18/netherlands-303419_960_720.png",
                xref = "x",
                yref = "y",
                x = 3.53,
                y = 53.65,
                sizex = 3.45,
                sizey = 3.0,
                sizing = "stretch",
                opacity = 0.5,
                layer = "below"))

    fig.show()



