"""
=================================================
Code.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Object based railway traject
=================================================
"""

class Station():
    "Station Object"
    def __init__(self):
        self.name = ''
        self.connections  = []
        self.visited = 0
        self.xcor = 0
        self.ycor = 0
        

class Model():
    "Railway Model"
    def __init__(self):
        self.stations = []
        self.traject = {}
        self.score = 0
    
    def fraction_visited(self):
        pass
    
    def quality_score(self):
        pass
        # return p * 10000 - (T * 100 + Min)

    
    def load_stations(self):
        with open(f"data_holland/StationsNationaal.csv") as f:
            while True:
                line = f.readline()
                line = line.split(",")

if __name__ == "__main__":
    station = Model()
    print(station.stations)

