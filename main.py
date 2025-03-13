import os
import glob
from simulation import Simulation
from simulation_from_file import SimulationFromFile
from visualization import Visualization
from inputs import Inputs
from storage_manager import StorageManager

VISUALISATION_FOLDER = "visualizations"
INPUT_FOLDER = "input_files"


def main() -> None:
    print(
        "\n \nThis is a simple program for simulating evolution of 2D cellular automata starting from random noise. Please have fun with it!\n \n"
    )
    if not os.path.exists(VISUALISATION_FOLDER):
        os.makedirs(VISUALISATION_FOLDER)
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)

    while True:
        simulation_settings = input(
            "Enter:\n 1 for normal settings,\n 2 for advanced settings,\n 3 for input from text file,\n anything else for default settings:"
        )

        if simulation_settings == "3":
            files = glob.glob(INPUT_FOLDER + "/*")
            if len(files) == 1:
                input_path = files[0]
            elif len(files) > 1:
                print("\ninput files:\n")
                for iter in range(len(files)):
                    print(str(iter + 1) + ": " + files[iter] + "\n")
                input_path = files[Inputs.input_file(len(files))]
            else:
                print("There are no input files. \n")
                break

            simulator = SimulationFromFile(
                Inputs.rules(), Inputs.n_steps(), input_path
            )
        elif simulation_settings == "2":
            simulator = Simulation(
                Inputs.grid_size(),
                Inputs.probability(),
                Inputs.rules(),
                Inputs.number_of_steps()
            )
        elif simulation_settings == "1":
            simulator = Simulation(
                100, 0.5, Inputs.rules(), Inputs.number_of_steps()
            )
        else:
            simulator = Simulation(100, 0.5, [[3], [3, 2]], 100)

        simulator.simulate()

        while True:
            visualization_settings = input(
                "Use advanced settings for making visualisation? ('Y' or 'y' count as yes; any other as no):\n"
            )

            if visualization_settings == "Y" or visualization_settings == "y":
                visualizer = Visualization(
                    Inputs.figsize(),
                    Inputs.frames_per_second(),
                    Inputs.number_of_frames(simulator.number_of_steps),
                    Inputs.animation_name(),
                    VISUALISATION_FOLDER,
                )

            else:
                visualizer = Visualization(
                    10,
                    5,
                    simulator.number_of_steps,
                    Inputs.animation_name(),
                    VISUALISATION_FOLDER,
                )

            visualizer.animate()

            another_animation = input(
                "Do you want to make another animation of this simulation? ('Y' or 'y' count as yes; any other as no):"
            )
            if not another_animation == "y" and not another_animation == "Y":
                break

        storage = StorageManager()
        storage.clear()

        another_simulation = input(
            "Do you want to run another simulation? ('Y' or 'y' count as yes; any other as no):"
        )
        if not another_simulation == "y" and not another_simulation == "Y":
            break

    print("Thank you for using my program!")


if __name__ == "__main__":
    main()
