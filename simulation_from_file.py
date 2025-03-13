import numpy as np
from simulation import Simulation
from storage_manager import StorageManager


class SimulationFromFile(Simulation):
    def __init__(
        self,
        rules: list[list[int]],
        number_of_steps: int,
        input_path: str,
    ) -> None:
        self.steps = 0
        self.sim_data = np.loadtxt(input_path)
        self.rules = rules
        self.number_of_steps = number_of_steps
        self.storage_manager =  StorageManager()
        self.size = len(self.sim_data)


        self.print_sim_settings()
        self.auxilliary_array = np.zeros((self.size, self.size), dtype="int")
