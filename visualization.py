import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc
from matplotlib import rcParams
from storage_manager import StorageManager


class Visualization:
    def __init__(
        self,
        figsize: float,
        frames_per_second: float,
        number_of_frames: int,
        animation_name: str,
        visualisation_folder: str,
    ) -> None:
        self.figsize = figsize
        self.frames_per_second = frames_per_second
        self.number_of_frames = number_of_frames
        self.animation_name = animation_name
        self.fig, self.ax = plt.subplots(figsize=(self.figsize, self.figsize))
        self.storage_manager = StorageManager()
        self.visualization_folder = visualisation_folder
        plt.tick_params(
            left=False, right=False, labelleft=False, labelbottom=False, bottom=False
        )

    def draw(self, i: int) -> None:
        """This method is used for generating a frame coresponding to i-th step of the simulation"""
        self.ax.clear()
        self.ax.imshow(self.storage_manager.read(i), cmap="Greys")
        plt.title("iteration" + str(i))

    def animate(self) -> None:
        """This method"""
        print("Animating...\n")
        ani = FuncAnimation(
            self.fig,
            self.draw,
            frames=self.number_of_frames,
            interval=1000 / self.frames_per_second,
            repeat=False,
        )
        rc("animation", html="html5")
        rcParams["animation.embed_limit"] = 2**128

        print("Saving the animation to file...\n")
        ani.save(self.visualization_folder + "/" + self.animation_name + ".gif")
