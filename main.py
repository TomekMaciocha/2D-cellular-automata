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
    storage = StorageManager()
    if not os.path.exists(VISUALISATION_FOLDER):
        os.makedirs(VISUALISATION_FOLDER)
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)

    while True:
        sim_settings = input(
            "Enter:\n 1 for normal settings,\n 2 for advanced settings,\n 3 for input from text file,\n anything else for default settings:"
        )

        if sim_settings == "3":
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

            sim = SimulationFromFile(
                Inputs.sim_rules(), Inputs.sim_n_steps(), input_path, storage
            )
        elif sim_settings == "2":
            sim = Simulation(
                Inputs.sim_size(),
                Inputs.sim_probability(),
                Inputs.sim_rules(),
                Inputs.sim_n_steps(),
                storage,
            )
        elif sim_settings == "1":
            sim = Simulation(
                100, 0.5, Inputs.sim_rules(), Inputs.sim_n_steps(), storage
            )
        else:
            sim = Simulation(100, 0.5, [[3], [3, 2]], 100, storage)

        sim.simulate()

        while True:
            vis_settings = input(
                "Use advanced settings for making visualisation? ('Y' or 'y' count as yes; any other as no):\n"
            )

            if vis_settings == "Y" or vis_settings == "y":
                vis = Visualization(
                    Inputs.vis_figsize(),
                    Inputs.vis_fps(),
                    Inputs.vis_n_frames(sim.n_steps),
                    Inputs.vis_animation_name(),
                    storage,
                    VISUALISATION_FOLDER,
                )

            else:
                vis = Visualization(
                    10,
                    5,
                    sim.n_steps,
                    Inputs.vis_animation_name(),
                    storage,
                    VISUALISATION_FOLDER,
                )

            vis.animate()

            another_ani = input(
                "Do you want to make another animation of this simulation? ('Y' or 'y' count as yes; any other as no):"
            )
            if not another_ani == "y" and not another_ani == "Y":
                break

        storage.clear()

        another_sim = input(
            "Do you want to run another simulation? ('Y' or 'y' count as yes; any other as no):"
        )
        if not another_sim == "y" and not another_sim == "Y":
            break

    print("Thank you for using my program!")


if __name__ == "__main__":
    main()
