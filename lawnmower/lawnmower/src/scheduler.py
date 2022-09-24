import lawnmower.src.lawn
import lawnmower.src.mower
import lawnmower.src.orientation


class Scheduler:
    """
        Schedules the execution of all mower instructions to clean the lawn.
    """
    def __init__(self, config_file, mower_overlapping=False):
        """
            Initializes the scheduler.

        :param config_file: (lawnmower.src.config_file.ConfigFile) Loaded info of the lawn to be cleaned and all mowers.
        :param mower_overlapping: (bool) If True more than one mower can be in the same cell of the lawn grid at the
            same time (big cells assumed). Otherwise, if a cell is occupied by one mower no other mower can enter that
            cell.
        :return: None
        """
        # Loaded configuration (lawnmower.src.config_file.ConfigFile)
        self.config_file = config_file

        # Tells if more than one mower can be in the same lawn grid cell (bool)
        self.mower_overlapping = mower_overlapping

        # Lawn info (lawnmower.src.lawn.Lawn)
        self.lawn = None

        # List of Mower Info after having executed all their instructions (i.e., final positions)
        # (list of lawnmower.src.mower.Mower)
        self.mowers = []

    def __repr__(self):
        result = ""

        try:
            for mower in self.mowers:
                result += "{} {} {}\n".format(mower.x, mower.y, mower.orientation.get_str())

        except (TypeError, AttributeError):
            # If no mowers simply ignore it.
            pass

        return result

    @staticmethod
    def print(message):
        """
            Prints the message.

            NOTE: For testability reasons only.

        :param message: (str) Message to be printed to the stdout.
        :return: None
        """
        print(message)

    @staticmethod
    def cprint(message, verbose=False):
        """
            Conditionally print the specified message (only if verbose is True).

        :param message: (str) Message to be printed to the stdout.
        :param verbose: (bool) If True prints out the message.
        :return: None
        """
        if verbose:
            Scheduler.print(message)

    def run(self, verbose=False):
        """
            Uses the loaded configuration to obtain all info, both from the lawn to be cleaned and the available mowers,
             required to clean the lawn. Each mower moves sequentially, it means that the second mower moves only after
             the first one executes all its instructions.

            IMPLEMENTATION NOTE: I decided to add additional verbosity to highly increase testability, although it
                slightly reduce code readability.

            TODO: For the sake of readability, split this long method into:
                    init_scheduler, init_mower, execute_mower_instructions

            TODO: For the sake of readability, parametrize cprint method to simply indicate the step
                    (i.e., single call per step)

        :param verbose: (bool) If True prints out intermediate steps in order to better visualize the whole process.
        :return: None
        """
        try:
            self.cprint("##############################################################", verbose)
            self.cprint("STEP  1.0 - Starting scheduler ... ", verbose)

            # Load Lawn info
            self.lawn = lawnmower.src.lawn.Lawn(x_max=self.config_file.lawn_x_max, y_max=self.config_file.lawn_y_max)
            self.mowers = []

            self.cprint("STEP  2.0 - Lawn initialized: {}".format(self.lawn), verbose)

            for mower_info in self.config_file.mowers:
                # Load Mower info
                self.cprint("----------------------------------------------------------------------", verbose)
                self.cprint("----------------------------------------------------------------------", verbose)
                self.cprint("STEP  3.0 - Initializing Mower #{}".format(len(self.mowers)), verbose)

                orientation = lawnmower.src.orientation.Orientation(orientation_str=mower_info["initial_orientation"])
                mower = lawnmower.src.mower.Mower(x=mower_info["initial_position"][0],
                                                  y=mower_info["initial_position"][1],
                                                  orientation=orientation, lawn=self.lawn)

                self.cprint("STEP  4.0", verbose)
                self.cprint("STEP  4.1 - initial position  X: {}".format(mower.x), verbose)
                self.cprint("STEP  4.1 - initial position  Y: {}".format(mower.y), verbose)
                self.cprint("STEP  4.1 - initial orientation: {}".format(mower.orientation.get_str()), verbose)
                self.cprint("STEP  4.2 - Starting to execute instructions: {} ...".format(
                    mower_info["instruction_list"]), verbose)

                # Execute current mower instructions
                for instruction in mower_info["instruction_list"]:

                    self.cprint("----------------------------------------------------------------------", verbose)
                    self.cprint("STEP  5.0 - instruction        : {}".format(instruction), verbose)
                    self.cprint("STEP  5.0 - mower_overlapping  : {}".format(self.mower_overlapping), verbose)
                    self.cprint("STEP  5.0 - current position  X: {}".format(mower.x), verbose)
                    self.cprint("STEP  5.0 - current position  Y: {}".format(mower.y), verbose)
                    self.cprint("STEP  5.0 - current orientation: {}".format(mower.orientation.get_str()), verbose)

                    if self.mower_overlapping:
                        # No need to care about prior mowers
                        self.cprint("STEP  6.0", verbose)

                        mower.execute(instruction=instruction)

                        self.cprint("STEP  7.0 - new           X: {}".format(mower.x), verbose)
                        self.cprint("STEP  7.0 - new           Y: {}".format(mower.y), verbose)
                        self.cprint("STEP  7.0 - new orientation: {}".format(mower.orientation.get_str()), verbose)

                    else:
                        # First, obtain the position after running the instruction
                        self.cprint("STEP  8.0", verbose)

                        next_x, next_y = mower.execute(instruction=instruction, dry_run_mode=True)

                        self.cprint("STEP  9.0 - next_x     : {}".format(next_x), verbose)
                        self.cprint("STEP 10.0 - next_y     : {}".format(next_y), verbose)
                        self.cprint("STEP 10.1 - orientation: {}".format(mower.orientation.get_str()), verbose)

                        if next_x is not None and next_y is not None:
                            self.cprint("STEP 11.0", verbose)

                            # There is a position modification. Check prior mowers' last position
                            mowers_collision = False

                            for prior_mower in self.mowers:
                                if next_x == prior_mower.x and next_y == prior_mower.y:
                                    mowers_collision = True
                                    break

                            self.cprint("STEP 12.0 - mowers_collision: {}".format(mowers_collision), verbose)

                            if not mowers_collision:
                                # If no collision execute. Otherwise, ignore it.
                                mower.execute(instruction=instruction)

                                self.cprint("STEP 13.0 - new position   X: {}".format(mower.x), verbose)
                                self.cprint("STEP 13.0 - new position   Y: {}".format(mower.y), verbose)
                                self.cprint("STEP 13.0 - new orientation : {}".format(mower.orientation.get_str()),
                                            verbose)

                        else:
                            # There is NO position modification. Proceed to really execute the instruction
                            mower.execute(instruction=instruction)

                            self.cprint("STEP 14.0 - new            X: {}".format(mower.x), verbose)
                            self.cprint("STEP 14.0 - new            Y: {}".format(mower.y), verbose)
                            self.cprint("STEP 14.0 - new orientation : {}".format(mower.orientation.get_str()), verbose)

                # The mower has finished executing all its instructions
                self.cprint("----------------------------------------------------------------------", verbose)
                self.cprint("STEP 15.0 - Mower #{} ".format(len(self.mowers)), verbose)
                self.cprint(".......................................", verbose)
                self.cprint("STEP 15.0 - FINAL position  X: {}".format(mower.x), verbose)
                self.cprint("STEP 15.0 - FINAL position  Y: {}".format(mower.y), verbose)
                self.cprint("STEP 15.0 - FINAL orientation: {}".format(mower.orientation.get_str()), verbose)

                self.mowers.append(mower)

                self.cprint("STEP 16.0", verbose)

        except AttributeError:
            print("ERROR while running scheduler : Missing valid config file")

        except TypeError:
            print("ERROR while running scheduler : Config file not properly loaded")

        self.cprint("STEP 17.0", verbose)
        self.cprint("##############################################################", verbose)
