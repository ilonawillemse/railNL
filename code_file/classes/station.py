"""
=================================================
station.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Station class for the railway model
Stations have a name, xcor and ycor and know the adjacent connecting stations
=================================================
"""


class Station:
    """
    Station object
    """

    def __init__(self, name, xcor, ycor):
        self.name = name
        self.connections = {}
        self.xcor = xcor
        self.ycor = ycor
