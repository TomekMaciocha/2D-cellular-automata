class Inputs:
    def input_file(max: int) -> int:
        """This method is used to manually choose an input file if there's more than one in the input folder."""
        print("Input the number of chosen input file:")
        while True:
            filenumber = input()
            if int(filenumber) < 1 or int(filenumber) > max:
                print("Input not in specified range.")
                continue
            return int(filenumber) - 1

    def grid_size() -> int:
        """This method is used to manually enter the size of the simulated system."""
        print("Set size of the simulation grid (3 to 1000, default: 100):")
        while True:
            size = input()
            if size == "":
                return 100
            elif int(size) < 3 or int(size) > 1000:
                print("Input not in specified range.")
                continue
            return int(size)

    def probability() -> float:
        """This method is used to manually enter the initial probability of cells being alive in the simulated system."""
        print(
            "Set probability of a cell being alive on the starting iteration (default: 0.5):"
        )
        while True:
            probability = input()
            if probability == "":
                return 0.5
            elif float(probability) < 0 or float(probability) > 1:
                print("Probability has to be between 0 and 1")
                continue
            return float(probability)

    def rules() -> list[list[int]]:
        """This method is used to manually enter the cellular automaton rules applying to the simulated system."""
        print(
            "Input numbers of alive neighbors required for a dead cell to become alive (0 to 8, none to end this setting):"
        )
        rules = [[], []]
        while True:
            proposed_rule = input()
            if proposed_rule == "":
                break
            elif int(proposed_rule) < 0 or int(proposed_rule) > 8:
                print("Input not in specified range.")
                continue
            elif int(proposed_rule) in rules[0]:
                print("This rule is already in place.")
                continue
            rules[0].append(int(proposed_rule))

        print(
            "Input numbers of alive neighbors required for an alive cell to stay alive (0 to 8, none to end this setting):"
        )

        while True:
            proposed_rule = input()
            if proposed_rule == "":
                break
            elif int(proposed_rule) < 0 or int(proposed_rule) > 8:
                print("Input not in specified range.")
                continue
            elif int(proposed_rule) in rules[1]:
                print("This rule is already in place.")
                continue
            rules[1].append(int(proposed_rule))
        return rules

    def number_of_steps() -> int:
        """This method is used to manually enter the length of the simulation to be performed."""
        number_of_steps = input("input number of steps in the simulation (default: 100):\n")
        if number_of_steps == "":
            return 100
        else:
            return int(number_of_steps)

    def figsize() -> float:
        """This method is used to manually enter the size of the figure used for generating animation frames."""
        print("Set size of the square figure used for generating frames (default: 10):")
        while True:
            size = input()
            if size == "":
                return 10
            elif float(size) <= 0:
                print("The size must be a positive number.")
                continue
            return float(size)

    def frames_per_second() -> float:
        """This method is used to manually enter the number of frames per second in the animation to be generated."""
        print(
            "Set number of frames per second in the animation (0.2 to 300, default: 5):"
        )
        while True:
            frames_per_second = input()
            if frames_per_second == "":
                return 5
            elif float(frames_per_second) < 0.2 or float(frames_per_second) > 300:
                print("Input not in specified range.")
                continue
            return float(frames_per_second)

    def number_of_frames(n_steps) -> int:
        """This method is used to manually enter the number of frames in the animation to be generated."""
        print(
            "Set number of frames in the animation (1 to "
            + str(n_steps)
            + ", default: "
            + str(n_steps)
            + "):"
        )
        while True:
            number_of_frames = input()
            if number_of_frames == "":
                return n_steps
            elif int(number_of_frames) < 1 or int(number_of_frames) > n_steps:
                print("Input not in specified range.")
                continue
            return int(number_of_frames)

    def animation_name() -> str:
        """This method is used to set the name of a file in which the generated animation will be saved"""
        print("Set the filename of the animation without extension (default: 'animation'):")
        name = input()
        if name == "":
            name = "animation"
        return name
