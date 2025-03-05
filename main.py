import os
import glob
from simulation import Simulation
from visualization import Visualization
from inputs import Inputs

OUTPUT_FOLDER = "output_files"
VISUALISATION_FOLDER = "visualizations"

def main() -> None:
    print(
        "\n \nThis is a simple program for simulating evolution of 2D cellular automata starting from random noise. Please have fun with it!\n \n"
    )

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    if not os.path.exists(VISUALISATION_FOLDER):
        os.makedirs(VISUALISATION_FOLDER)

    while True:
        sim_settings = input(
            "Enter 1 for normal settings, 2 for advanced settings, anything else for default settings:"
        )

        if sim_settings == "2":
            sim = Simulation(
                Inputs.sim_size(),
                Inputs.sim_probability(),
                Inputs.sim_rules(),
                Inputs.sim_n_steps(),
                OUTPUT_FOLDER,
            )
        elif sim_settings == "1":
            sim = Simulation(
                100, 0.5, Inputs.sim_rules(), Inputs.sim_n_steps(), OUTPUT_FOLDER
            )
        else:
            sim = Simulation(100, 0.5, [[3], [3, 2]], 100, OUTPUT_FOLDER)

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
                    OUTPUT_FOLDER,
                    VISUALISATION_FOLDER,
                )

            else:
                vis = Visualization(
                    10,
                    5,
                    sim.n_steps,
                    Inputs.vis_animation_name(),
                    OUTPUT_FOLDER,
                    VISUALISATION_FOLDER,
                )

            vis.animate()

            another_ani = input(
                "Do you want to make another animation of this simulation? ('Y' or 'y' count as yes; any other as no):"
            )
            if not another_ani == "y" and not another_ani == "Y":
                break

        files = glob.glob("output_files/*")
        for f in files:
            os.remove(f)

        another_sim = input(
            "Do you want to run another simulation? ('Y' or 'y' count as yes; any other as no):"
        )
        if not another_sim == "y" and not another_sim == "Y":
            break

    print("Thank you for using my program!")


if __name__ == "__main__":
    main()
