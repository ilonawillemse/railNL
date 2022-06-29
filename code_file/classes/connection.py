"""
=================================================
connection.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Connection class for the railway model
Connections know the starting and ending stations with their corresponding duration time
to travel the connection and an id
=================================================
"""


class Connection:
    """
    Object for a connection between stations
    """

    def __init__(self, station_1, station_2, time, id):
        self.start = station_1
        self.end = station_2
        self.visit = 0
        self.duration = time
        self.id = id
