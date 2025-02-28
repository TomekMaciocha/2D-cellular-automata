import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc
from matplotlib import rcParams
import os


class Visualization:
    def __init__(
        self,
    ) -> None:
        self.advanced_settings = input(
            "Use advanced settings for making visualisation? ('Y' or 'y' count as yes; any other as no):\n"
        )
        self.max_len = 0

        while True:
            tmp = os.path.isfile("output_files/state" + str(self.max_len) + ".txt")
            self.max_len += tmp
            if not tmp:
                break

        if self.advanced_settings == "Y" or self.advanced_settings == "y":
            self.set_figsize()
            self.set_fps()
            self.set_nsteps()
        else:
            self.figsize = 10
            self.fps = 5
            self.nsteps = self.max_len

        self.fig, self.ax = plt.subplots(figsize=(self.figsize, self.figsize))
        plt.tick_params(
            left=False, right=False, labelleft=False, labelbottom=False, bottom=False
        )

    def set_figsize(self) -> None:
        print("Set size of the square figure used for generating frames (default: 10):")
        while True:
            tmp = input()
            if tmp == "":
                self.figsize = 10
                break
            elif float(tmp) <= 0:
                print("The size must be a positive number.")
                continue
            self.figsize = tmp
            break

    def set_fps(self) -> None:
        print(
            "Set number of frames per second in the animation (0.2 to 1000, default: 5):"
        )
        while True:
            tmp = input()
            if tmp == "":
                self.fps = 5
                break
            elif float(tmp) < 0.2 or float(tmp) > 1000:
                print("Input not in specified range.")
                continue
            self.fps = tmp
            break

    def set_nsteps(self) -> None:
        print(
            "Set number of frames in the animation (1 to "
            + str(self.max_len)
            + ", default: "
            + str(self.max_len)
            + "):"
        )
        while True:
            tmp = input()
            if tmp == "":
                self.nsteps = self.max_len
                break
            elif int(tmp) < 1 or int(tmp) > self.max_len:
                print("Input not in specified range.")
                continue
            self.nsteps = tmp
            break

    def draw(self, i: int) -> None:
        self.ax.clear()
        self.ax.imshow(np.loadtxt("output_files/state" + str(i) + ".txt"), cmap="Greys")
        plt.title("iteration" + str(i))

    def animate(self) -> None:
        ani = FuncAnimation(
            self.fig,
            self.draw,
            frames=self.nsteps,
            interval=1000 / self.fps,
            repeat=False,
        )
        rc("animation", html="html5")
        rcParams["animation.embed_limit"] = 2**128

        print("Set the filename of the animation without extension (default: 'ani'):")

        tmp = input()
        if tmp == "":
            tmp = "ani"

        ani.save("visualizations/" + tmp + ".gif")
