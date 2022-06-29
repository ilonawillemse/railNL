"""
=================================================
dataclass.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Dataclass class to initialize some variables
=================================================
"""


class Dataclass:
    "Dataclass Object"

    def __init__(self):
        self.best_score = 0
        self.counter = 0
        self.best_fraction = 0
        self.best_traject = 0
        self.best_traject = []
        self.all_data = []
        self.duration = []
        self.RUNNING_TIME = 1800
        self.plot_data = []
        self.TOTAL_ITERATIONS = 15000
