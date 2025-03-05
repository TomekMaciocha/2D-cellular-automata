
class Inputs:

    def input_file(max:int) ->int:
        '''This method is used to manually choose an input file if there's more than one in the input folder.'''
        print("Input the number of chosen input file:")
        while True:
            tmp = input()
            if int(tmp) < 1 or int(tmp) > max:
                print("Input not in specified range.")
                continue
            return int(tmp)-1

    def sim_size() -> int:
        """This method is used to manually enter the size of the simulated system."""
        print("Set size of the simulation grid (3 to 1000, default: 100):")
        while True:
            tmp = input()
            if tmp == "":
                return 100
            elif int(tmp) < 3 or int(tmp) > 1000:
                print("Input not in specified range.")
                continue
            return int(tmp)


    def sim_probability() -> float:
        """This method is used to manually enter the initial probability of cells being alive in the simulated system."""
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


    def sim_rules() -> list[list[int]]:
        """This method is used to manually enter the cellular automaton rules applying to the simulated system."""
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


    def sim_n_steps() -> int:
        """This method is used to manually enter the length of the simulation to be performed."""
        tmp = input("input number of steps in the simulation (default: 100):\n")
        if tmp == "":
            return 100
        else:
            return int(tmp)


    def vis_figsize() -> float:
        """This method is used to manually enter the size of the figure used for generating animation frames."""
        print("Set size of the square figure used for generating frames (default: 10):")
        while True:
            tmp = input()
            if tmp == "":
                return 10
            elif float(tmp) <= 0:
                print("The size must be a positive number.")
                continue
            return float(tmp)


    def vis_fps() -> float:
        """This method is used to manually enter the number of frames per second in the animation to be generated."""
        print("Set number of frames per second in the animation (0.2 to 300, default: 5):")
        while True:
            tmp = input()
            if tmp == "":
                return 5
            elif float(tmp) < 0.2 or float(tmp) > 300:
                print("Input not in specified range.")
                continue
            return float(tmp)


    def vis_n_frames(n_steps) -> int:
        """This method is used to manually enter the number of frames in the animation to be generated."""
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


    def vis_animation_name() -> str:
        """This method is used to set the name of a file in which the generated animation will be saved"""
        print("Set the filename of the animation without extension (default: 'ani'):")
        tmp = input()
        if tmp == "":
            tmp = "ani"
        return tmp
