import numpy as np
from simulation import Simulation

class SimulationFromFile(Simulation):

    def __init__(
        self, rules: list[list[int]], n_steps: int,input_path:str, output_folder:str
    ) -> None:
        self.steps = 0
        self.sim_data = np.loadtxt(input_path)
        self.rules = rules
        self.n_steps=n_steps
        self.output_folder = output_folder
        self.size = len(self.sim_data)

        self.print_sim_settings()
        self.temp = np.zeros((self.size, self.size), dtype="int")

