import traceback


class ConfigFile:
    """
        Mower Configuration File.

        * The first line is the coordinates of the upper-right corner of the lawn, coordinates of lower-left
        corner are supposed to be (0,0)

        * Next lines of the file drive all mowers. There are two lines for each mower:

            * First line give the initial position and orientation of the mower. Position and orientation are given
            by 2 numbers and a letter, separated by a space

            * Second line is a sequence of instruction driving the mower across the lawn. Instructions are a
            sequence of letters without space.

        Example:

                5 5
                1 2 N
                LFLFLFLFF
                3 3 E
                FFRFFRFRRF
    """
    def __init__(self):
        # Coordinate X of the upper-right corner of the lawn (int)
        self.lawn_x_max = None

        # Coordinate X of the upper-right corner of the lawn (int)
        self.lawn_y_max = None

        # List of mowers (list of dicts)
        # For each mower, stored in order of appearance, there will be three pairs of key-values
        #
        #     initial_position (tuple of str): with (X, Y) being the coordinates of the initial position of the mower.
        #     initial_orientation (str): A letter indicating the initial orientation of the mower.
        #     instruction_list (str): String with as many characters as instructions, and in the same chronological
        #           order of execution, to be executed for that mower.
        #
        self.mowers = []

    @staticmethod
    def open_file(*args, **kwargs):
        """
            Opens a file (see Python built-in open in https://docs.python.org/3/library/functions.html#open)

            NOTE: For improved testability reasons only.
        """
        return open(*args, **kwargs)

    def load(self, filepath):
        """
            Reads the specified file and updates the information according to its contain.

            TODO: For the sake of readability, split this long method into:
                    get_lawn_info, get_next_mower_position_and_orientation, get_next_mower_instructions


        :param filepath: (str) Path to the configuration file to be loaded.
        :return: (bool) True if the file was successfully loaded; False otherwise.
        """
        result = False

        try:
            with self.open_file(filepath) as f:
                # Add lawn info
                line = f.readline().replace("\n", "")
                try:
                    lawn_x_max, lawn_y_max = line.split()

                except ValueError:
                    print("ERROR while loading configuration file '{}' : Invalid format in line 1 '{}'".format(filepath,
                                                                                                               line))
                    line = ""

                mowers = []
                # print("\nSTEP 1 - line: {}".format(line))  # DEBUGGING

                while line:
                    #
                    # Add info of the next mower
                    #
                    # print("STEP 2 - line: {}".format(line))  # DEBUGGING
                    try:
                        #
                        # Initial position and orientation
                        #
                        line = f.readline().replace("\n", "")
                        # print("STEP 3 - line: {}".format(line))  # DEBUGGING
                        line_parts = line.split()
                        new_mower = {"initial_position": (line_parts[0], line_parts[1]),
                                     "initial_orientation": line_parts[2]}

                    except IndexError:
                        # print("STEP 4")  # DEBUGGING

                        if not line and len(mowers) == 0:
                            # print("STEP 5")  # DEBUGGING
                            print("ERROR while loading configuration file '{}' : Invalid format - Missing mowers "
                                  "info in line {}".format(filepath, 2 * (len(mowers) + 1)))

                        elif line:
                            # print("STEP 6")  # DEBUGGING
                            print("ERROR while loading configuration file '{}' : Invalid format in line {}".format(
                                filepath, 2 * (len(mowers) + 1)))

                        else:
                            # In this case there is NO error. Already read valid info
                            result = True
                            # print("STEP 7")  # DEBUGGING
                            break

                        # print("STEP 8")  # DEBUGGING
                        return result

                    #
                    # Instruction list
                    #
                    line = f.readline().replace("\n", "")
                    # print("STEP 9")  # DEBUGGING

                    if line:
                        new_mower.update({"instruction_list": line})
                        mowers.append(new_mower)
                        # print("STEP 10")  # DEBUGGING
                    else:
                        print("ERROR while loading configuration file '{}' : Invalid format - Missing mower #{} "
                              "instructions info in line {}".format(filepath, len(mowers) + 1,
                                                                    2 * (len(mowers) + 1) + 1))
                        # print("STEP 11")  # DEBUGGING
                        return result

                # print("STEP 12")  # DEBUGGING
                if len(mowers) > 0:
                    # If everything is OK, update the loaded configuration
                    self.lawn_x_max = lawn_x_max
                    self.lawn_y_max = lawn_y_max
                    self.mowers = mowers
                    result = True

        except TypeError:
            print("ERROR while loading configuration : Invalid filepath '{}'".format(filepath))

        except FileNotFoundError:
            print("ERROR while loading configuration : File not found '{}'".format(filepath))

        except Exception as e:
            print("Unexpected ERROR while loading configuration from file '{}' : {}\n{}".format(filepath, e,
                                                                                                traceback.format_exc()))

        return result
