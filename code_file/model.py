from code_file.loader import load_stations, add_connections
from code_file.algorithms.baseline import starting_trajects
from code_file.helpers import quality_score
from code_file.algorithms.greedy import get_started


class Model:
    """
    Railway Model
    Stores the stations and connections
    Keeps track of the connections that have already been visited
    Stores the trajects when made
    Keeps track of the duration of the trajects
    Keeps track of the quality scores, the fraction of visited connections,
        the number of trajects and the total time it takes
    """

    def __init__(self):
        self.stations = load_stations()
        self.all_connections = add_connections(self.stations)
        self.visited_connections = []
        self.traject = []
        self.time_dict = {}
        self.score, self.fraction, self.number_traject, self.total_time = 0, 0, 0, 0

    def baseline(self):
        starting_trajects(self)
        quality_score(self)

    def greedy(self):
        get_started(self)
        quality_score(self)
