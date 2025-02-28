import os
import glob
from simulation import Simulation
from visualization import Visualization


def main() -> None:
    os.system("cls")
    print(
        "\n \nThis is a simple program for simulating evolution of 2D cellular automata starting from random noise. Please have fun with it!\n \n"
    )

    while True:
        sim = Simulation()
        sim.simulate()

        while True:
            vis = Visualization()
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
