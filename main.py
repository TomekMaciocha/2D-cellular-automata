import os
import glob
from simulation import Simulation
from visualization import Visualization

OUTPUT_FOLDER = "output_files"
VISUALISATION_FOLDER = "visualizations"


def sim_set_size() -> int:
    """This function is used to manually enter the size of the simulated system."""
    print("Set size of the simulation grid (3 to 1000, default: 100):")
    while True:
        tmp = input()
        if tmp == "":
            return 100
        elif int(tmp) < 3 or int(tmp) > 1000:
            print("Input not in specified range.")
            continue
        return int(tmp)


def sim_set_probability() -> float:
    """This function is used to manually enter the initial probability of cells being alive in the simulated system."""
    print(
        "Set probability of a cell being alive on the starting iteration (default: 0.5):"
    )
    while True:
        tmp = input()
        if tmp == "":
            return 0.5
        elif float(tmp) < 0 or float(tmp) > 1:
            print("Probability has to be between 0 and 1")
            continue
        return float(tmp)


def sim_set_rules() -> list[list[int]]:
    """This function is used to manually enter the cellular automaton rules applying to the simulated system."""
    print(
        "Input numbers of alive neighbors required for a dead cell to become alive (0 to 8, none to end this setting):"
    )
    rules = [[], []]
    tmp = 1
    while True:
        tmp = input()
        if tmp == "":
            break
        elif int(tmp) < 0 or int(tmp) > 8:
            print("Input not in specified range.")
            continue
        elif int(tmp) in rules[0]:
            print("This rule is already in place.")
            continue
        rules[0].append(int(tmp))

    print(
        "Input numbers of alive neighbors required for an alive cell to stay alive (0 to 8, none to end this setting):"
    )

    tmp = 1
    while True:
        tmp = input()
        if tmp == "":
            break
        elif int(tmp) < 0 or int(tmp) > 8:
            print("Input not in specified range.")
            continue
        elif int(tmp) in rules[1]:
            print("This rule is already in place.")
            continue
        rules[1].append(int(tmp))
    return rules


def sim_set_n_steps() -> int:
    """This function is used to manually enter the length of the simulation to be performed."""
    tmp = input("input number of steps in the simulation (default: 100):\n")
    if tmp == "":
        return 100
    else:
        return int(tmp)


def vis_set_figsize() -> float:
    """This function is used to manually enter the size of the figure used for generating animation frames."""
    print("Set size of the square figure used for generating frames (default: 10):")
    while True:
        tmp = input()
        if tmp == "":
            return 10
        elif float(tmp) <= 0:
            print("The size must be a positive number.")
            continue
        return float(tmp)


def vis_set_fps() -> float:
    """This function is used to manually enter the number of frames per second in the animation to be generated."""
    print("Set number of frames per second in the animation (0.2 to 300, default: 5):")
    while True:
        tmp = input()
        if tmp == "":
            return 5
        elif float(tmp) < 0.2 or float(tmp) > 300:
            print("Input not in specified range.")
            continue
        return float(tmp)


def vis_set_n_frames(n_steps) -> int:
    """This function is used to manually enter the number of frames in the animation to be generated."""
    print(
        "Set number of frames in the animation (1 to "
        + str(n_steps)
        + ", default: "
        + str(n_steps)
        + "):"
    )
    while True:
        tmp = input()
        if tmp == "":
            return n_steps
        elif int(tmp) < 1 or int(tmp) > n_steps:
            print("Input not in specified range.")
            continue
        return int(tmp)


def vis_set_animation_name() -> str:
    """This function is used to set the name of a file in which the generated animation will be saved"""
    print("Set the filename of the animation without extension (default: 'ani'):")
    tmp = input()
    if tmp == "":
        tmp = "ani"
    return tmp


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
                sim_set_size(),
                sim_set_probability(),
                sim_set_rules(),
                sim_set_n_steps(),
                OUTPUT_FOLDER,
            )
        elif sim_settings == "1":
            sim = Simulation(
                100, 0.5, sim_set_rules(), sim_set_n_steps(), OUTPUT_FOLDER
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
                    vis_set_figsize(),
                    vis_set_fps(),
                    vis_set_n_frames(sim.n_steps),
                    vis_set_animation_name(),
                    OUTPUT_FOLDER,
                    VISUALISATION_FOLDER,
                )

            else:
                vis = Visualization(
                    10,
                    5,
                    sim.n_steps,
                    vis_set_animation_name(),
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
