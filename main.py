"""
=================================================
main.py

Ilona Willemse, Wesley Korff, Anouk Van Valkengoed

No way, Railway

Model for an object based railway traject
Interactive for user, based on with what algorithm they would like to run the simulation
The model contains two base algorithms to run the program with (random and greedy)
The programm generates an output file with the best trajects found
    and its corresponding quality score
Posibility to visualize the output file with trajects in a simulation
    - the moving dots are shown for fun, they repesent trains riding the trajects
    - dots move randomly across the traject, no transportations are meant to be visualized
=================================================
"""

from code_file.helpers import output_generate
from code_file.visualize_output import visualization_output
from code_file.plot import make_plot
from code_file.classes import Dataclass
from code_file.runs.run_algorithm import (
    run_hillclimber,
    run_repeated_simulated_annealing,
    run_simple,
)

if __name__ == "__main__":
    dataclass = Dataclass()
    type_hillclimber = None

    key = int(
        input(
            "What would you like to run: simple run(0), with hillclimber(1), "
            + "simulated annealing(2), simulate output file(3): "
        )
    )

    if key == 1:
        type_hillclimber = int(input("random(0) or worst traject removal(1): "))

    if key != 3:
        type_base = int(input("random(0) or greedy(1): "))

    if key == 3:
        visualization_output()

    # ---------------------run algorithm--------------------
    if key == 0:
        run_simple(type_base, dataclass)

    if key == 1:
        run_hillclimber(type_base, type_hillclimber, dataclass)

    if key == 2:
        run_repeated_simulated_annealing(type_base, dataclass)

    # generates an outputfile with the best trajects found and its corresponding quality score
    output_generate(dataclass.best_traject, dataclass.best_score)

    if key != 3:
        # plot with the corresponding gattered data
        make_plot(type_base, dataclass.all_data, key, dataclass.RUNNING_TIME)
