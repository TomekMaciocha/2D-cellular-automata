import numpy as np
from storage_manager import StorageManager


class Simulation:
    """A class for representing and simulating a 2D automaton on a grid, starting from random noise"""

    simulation_data = [[None]]
    auxilliary_array = [[None]]

    def __init__(
        self,
        size: int,
        probability: float,
        rules: list[list[int]],
        number_of_steps: int,
    ) -> None:
        self.steps = 0
        self.size = size
        self.probability = probability
        self.rules = rules
        self.number_of_steps = number_of_steps
        self.storage_manager = StorageManager()

        self.print_sim_settings()
        self.generate()
        self.auxilliary_array = np.zeros((self.size, self.size), dtype="int")

    def generate(self) -> None:
        """This method generates a random initial state of the system"""
        self.simulation_data = (
            np.random.random(size=(self.size, self.size)) < self.probability
        ).astype(int)

    def print_sim_settings(self) -> None:
        """This method prints out all the customisable variables in the class instance."""
        print("\n rules for dead cells becoming alive:" + str(self.rules[0]))
        print("\n rules for alive cells staying alive:" + str(self.rules[1]))
        print("\n grid size:" + str(self.size))
        print(
            "\n initial probability of cells being alive:"
            + str(self.probability)
            + "\n"
        )
        print(
            "\n number of steps in the simulation:" + str(self.number_of_steps) + "\n"
        )

    def is_alive(self, rows: int, cols: int) -> int:
        """This method determines next state of given cell based on number of alive neighbors and automaton rules."""
        num_neighbors = int(
            self.simulation_data[(rows - 1)][cols]
            + self.simulation_data[(rows - 1)][(cols - 1)]
            + self.simulation_data[(rows - 1)][(cols + 1) % self.size]
            + self.simulation_data[rows][(cols - 1)]
            + self.simulation_data[rows][(cols + 1) % self.size]
            + self.simulation_data[(rows + 1) % self.size][(cols - 1)]
            + self.simulation_data[(rows + 1) % self.size][cols]
            + self.simulation_data[(rows + 1) % self.size][(cols + 1) % self.size]
        )

        if self.simulation_data[rows][cols] == 0:
            return num_neighbors in self.rules[0]
        else:
            return num_neighbors in self.rules[1]

    def step(self) -> None:
        """This method advances the system by one step."""
        for i in range(self.size):
            for j in range(self.size):
                self.auxilliary_array[i][j] = self.is_alive(i, j)
        self.simulation_data = np.copy(self.auxilliary_array)

    def simulate(self) -> None:
        """This method runs the simulation based on parameters specified in the instance."""
        print("simulating...\n")
        self.storage_manager.write(self.simulation_data)
        for iter in range(self.number_of_steps):
            self.step()
            self.steps += 1
            self.storage_manager.write(self.simulation_data)
