import numpy as np
from simulation import Simulation
from storage_manager import StorageManager


class SimulationFromFile(Simulation):
    def __init__(
        self,
        rules: list[list[int]],
        n_steps: int,
        input_path: str,
        storage_manager: StorageManager,
    ) -> None:
        self.steps = 0
        self.sim_data = np.loadtxt(input_path)
        self.rules = rules
        self.n_steps = n_steps
        self.storage_manager = storage_manager
        self.size = len(self.sim_data)

        self.print_sim_settings()
        self.temp = np.zeros((self.size, self.size), dtype="int")
