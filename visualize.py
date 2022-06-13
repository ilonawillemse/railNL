
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