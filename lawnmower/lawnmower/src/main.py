import sys

import lawnmower.src.utils
import lawnmower.src.config_file
import lawnmower.src.scheduler


def get_arguments():
    """
        Gets arguments from command line.

        NOTE : If no arguments are given prints to stdout an error message, since input_filepath is mandatory.

    :return: (tuple)   (<input_filepath>, <verbose>, <mower_overlapping>)

            with:

            <input_filepath> : (str) The path to the text file including all configuration details.
            <verbose> : (bool) If True the output does not only include the final position/orientation of each mower
                            but all intermediate steps.

            <mower_overlapping> : (bool) If True the lawn grid cells are large enough to assume more than a single
                        mower can move/stay in the same cell without interfering each other.
    """
    mower_overlapping = False
    verbose = False
    input_filepath = ""

    if len(sys.argv) > 3:
        mower_overlapping = lawnmower.src.utils.get_bool_from_str(sys.argv[3])

    if len(sys.argv) > 2:
        verbose = lawnmower.src.utils.get_bool_from_str(sys.argv[2])

    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    else:
        print("ERROR : missing input_filepath")
        print("use   : {} <input_filepath> [<verbose>] [<mower_overlapping>]".format(sys.argv[0]))
        print("\n <input_filepath>    : The path to the text file including all configuration details."
              "\n <verbose>           : If True (True, T, t, Yes, Y, y, 1) the output does not only include the final "
              "\n                       position/orientation of each mower but all intermediate steps."
              "\n <mower_overlapping> : If True (True, T, t, Yes, Y, y, 1) the lawn grid cells are large enough to "
              "\n                       assume more than a single mower can move/stay in the same cell without "
              "\n                       interfering each other.\n")

    return input_filepath, verbose, mower_overlapping


def main():
    # Get arguments
    input_filepath, verbose, mower_overlapping = get_arguments()

    if input_filepath:
        # Load configuration
        config_file = lawnmower.src.config_file.ConfigFile()

        if config_file.load(input_filepath):
            # Create and run scheduler
            scheduler = lawnmower.src.scheduler.Scheduler(config_file=config_file, mower_overlapping=mower_overlapping)
            scheduler.run(verbose=verbose)
            print(scheduler)


if __name__ == "__main__":
    main()
