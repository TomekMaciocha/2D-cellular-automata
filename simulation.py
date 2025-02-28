import numpy as np


class Simulation:
    """A class for representing and simulating a 2D automaton on a grid, starting from random noise"""

    sim_data = [[None]]
    temp = [[None]]

    def __init__(
        self,
    ) -> None:
        self.steps = 0
        self.settings = input(
            "Enter 1 for normal settings, 2 for advanced settings, anything else for default settings:"
        )

        if self.settings == "2":
            self.set_rules()
            self.set_p()
            self.set_size()

        elif self.settings == "1":
            self.set_rules()
            self.p = 0.5
            self.size = 100
        else:
            self.rules = [[3], [3, 2]]
            self.p = 0.5
            self.size = 100

        self.gen()
        self.temp = np.zeros((self.size, self.size), dtype="int")
        self.settings_out()

    def set_p(self) -> None:
        print(
            "Set probability of a cell being alive on the starting iteration (default: 0.5):"
        )
        while True:
            tmp = input()
            if tmp == "":
                self.p = 0.5
                break
            elif float(tmp) < 0 or float(tmp) > 1:
                print("Probability has to be between 0 and 1")
                continue
            self.p = tmp
            break

    def gen(self) -> None:
        self.sim_data = (np.random.random(size=(self.size, self.size)) < self.p).astype(
            int
        )

    def settings_out(self) -> None:
        print("\n rules for dead cells:" + str(self.rules[0]))
        print("\n rules for alive cells:" + str(self.rules[1]))
        print("\n grid size:" + str(self.size))
        print("\n probability p:" + str(self.p) + "\n")

    def set_size(self) -> None:
        print("Set size of the simulation grid (3 to 1000, default: 100):")
        while True:
            tmp = input()
            if tmp == "":
                self.size = 100
                break
            elif int(tmp) < 3 or int(tmp) > 1000:
                print("Input not in specified range.")
                continue
            self.size = tmp
            break

    def set_rules(self) -> None:
        print("Input rules for when a cell is dead (0 to 8, none to end this setting):")
        self.rules = [[], []]
        tmp = 1
        while True:
            tmp = input()
            if tmp == "":
                break
            elif int(tmp) < 0 or int(tmp) > 8:
                print("Input not in specified range.")
                continue
            elif int(tmp) in self.rules[0]:
                print("This rule is already in place.")
                continue
            self.rules[0].append(int(tmp))

        print(
            "Input rules for when a cell is alive (0 to 8, none to end this setting):"
        )

        tmp = 1
        while True:
            tmp = input()
            if tmp == "":
                break
            elif int(tmp) < 0 or int(tmp) > 8:
                print("Input not in specified range.")
                continue
            elif int(tmp) in self.rules[1]:
                print("This rule is already in place.")
                continue
            self.rules[1].append(int(tmp))

    # This function returns the next state of a cell represented by arr[rows,cols] based on rules of the Conway's Game of Life.
    def Is_Alive(self, rows: int, cols: int) -> int:
        num_neighbors = int(
            self.sim_data[(rows - 1)][cols]
            + self.sim_data[(rows - 1)][(cols - 1)]
            + self.sim_data[(rows - 1)][(cols + 1) % self.size]
            + self.sim_data[rows][(cols - 1)]
            + self.sim_data[rows][(cols + 1) % self.size]
            + self.sim_data[(rows + 1) % self.size][(cols - 1)]
            + self.sim_data[(rows + 1) % self.size][cols]
            + self.sim_data[(rows + 1) % self.size][(cols + 1) % self.size]
        )

        if self.sim_data[rows][cols] == 0:
            return num_neighbors in self.rules[0]
        else:
            return num_neighbors in self.rules[1]

    # This function takes a state of a system in the form of a 2D array as an argument and returns an array representing state of the system in the next iteration.
    def step(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                self.temp[i][j] = self.Is_Alive(i, j)
        self.sim_data = np.copy(self.temp)

    def write_current(self, filename: str) -> None:
        np.savetxt("output_files/" + filename, np.array(self.sim_data), fmt="%d")

    def simulate(self) -> None:
        do_write = input("input an number of steps in the simulation (default: 200):\n")
        if do_write == "":
            nsteps = 200
        else:
            nsteps = int(do_write)
        self.write_current("state0.txt")
        for iter in range(nsteps):
            self.step()
            self.steps += 1
            self.write_current("state" + str(self.steps) + ".txt")
