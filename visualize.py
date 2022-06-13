
from copy import deepcopy
import plotly.graph_objects as go

def visualization(model, best_traject):
    "visualize the trajects with trains riding them"

    x_cor = []
    y_cor = []
    name = []
    connection_list = []

    for _, value in model.all_connections.items():
        connection_x_cor = []
        connection_y_cor = []

        connection_x_cor.append(float(value.start.ycor))
        connection_y_cor.append(float(value.start.xcor))
        connection_y_cor.append(float(value.end.xcor))
        connection_x_cor.append(float(value.end.ycor))

        connection = go.Scatter(x = connection_x_cor, y = connection_y_cor, line=dict(color="grey"))
        connection_list.append(connection)

    connection_list.append(go.Scatter(x = x_cor, y = y_cor, mode = "markers", hovertext= name, marker=dict(color="lightgreen"),opacity= 0.6 ))
    connection_list.insert(0, connection)
    
    # add moving trains to the trajects
    # make the train move back and forth for i steps

    total_list_x_cor = []
    total_list_y_cor = []
    
    for i in range(len(best_traject)):
        counter = 0
        list_y_cor = []
        list_x_cor = []
       
        while counter < 10:
            for j in range(len(best_traject[i])):
                if counter == 10:
                    break
                
                # x and y coordinates were switched in the csv file
                list_y_cor.append(float(best_traject[i][j].xcor))
                list_x_cor.append(float(best_traject[i][j].ycor))
                counter += 1

            for k in range(len(best_traject[i])-2 , 0, -1):
                if counter == 10:
                    break

                list_y_cor.append(float(best_traject[i][k].xcor))
                list_x_cor.append(float(best_traject[i][k].ycor))
                counter += 1
        
        # create a list of lists with coordinates of the train trajects
        total_list_x_cor.append(list_x_cor)
        total_list_y_cor.append(list_y_cor)


    final_list_x_cor = []
    final_list_y_cor = []
    current_list = []
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'grey', 'white']

    # comprehend the first coordinates of the trains depending on the number of trains
    # making them ride together
    for i in range(len(list_x_cor)):
        final_list_x_cor = [item[i] for item in total_list_x_cor]
        final_list_y_cor = [item[i] for item in total_list_y_cor]

        current = go.Frame(data=[go.Scatter(
                            x = final_list_x_cor, 
                            y = final_list_y_cor, 
                            mode = "markers", 
                            marker=dict(color=colors, size = 15))], 
                            layout=go.Layout(title_text="No way, railway"))
        current_list.append(current)
        

    # create the figure with connections/ stations and trains
    fig = go.Figure(
        data= connection_list,
        layout=go.Layout(
        xaxis=dict(range=[3.5, 6.5], autorange=False),
        yaxis=dict(range=[51, 54], autorange=False),
        title="No way, railway",
        showlegend = False,
        template = "plotly_white",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Let's rail",
                        method="animate",
                        args=[None, 
                            {'frame': { "duration": 1000, "redraw": True},}
                            ])])]),
                        
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
    fig.show()