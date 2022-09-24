class Orientation:
    """
        Handles orientation issues.
    """

    # In order to efficiently handle orientation changes, it is represented with an integer value (mod 4). Thus,
    #   turning 90 degrees to the right involves adding 1 whilst turning 90 degrees to the left involves subtracting 1.
    int_to_str = {
        0: "N",     # North
        1: "E",     # East
        2: "S",     # South
        3: "W"      # West
    }

    str_to_int = {value: key for key, value in int_to_str.items()}

    def __init__(self, orientation_str=None):
        """
            Initializes the orientation.

        :param orientation_str: (str) Initial orientation.
        :return: None
        """
        try:
            if orientation_str in self.str_to_int:
                # Only initialize with specified orientation in case of a valid orientation
                self.orientation = self.str_to_int[orientation_str]

            else:
                # North orientation by default

                # Current orientation, represented as an integer value
                self.orientation = 0

        except TypeError:
            # North orientation by default if invalid orientation specified

            # Current orientation, represented as an integer value
            self.orientation = 0

    def get_str(self):
        """
            Gets the current orientation as a string.

        :return: (str) Current orientation. Returns None in case of error.
        """
        try:
            return self.int_to_str[self.orientation]

        except (KeyError, TypeError):
            return None

    def set(self, orientation_str):
        """
            Sets the current orientation according to the specified one.

        :param orientation_str: (str) Current orientation.
        :return: None.
        """
        try:
            self.orientation = self.str_to_int[orientation_str]

        except (KeyError, TypeError):
            print("ERROR while setting orientation : Invalid orientation '{}' (Valid values: {})".format(
                orientation_str, list(self.str_to_int.keys())))

    def rotate(self, right=True):
        """
            Modifies the current orientation according to the specified direction.

        :param right: (bool) True indicates rotating 90 degrees to the right. False indicates rotating 90 degrees to
                        the left.
        :return: None
        """
        try:
            if self.orientation < 0 or self.orientation >= len(self.int_to_str):
                print("ERROR while rotating : Invalid orientation '{}'".format(self.orientation))
                print("Recalibrating to '{}' ...".format(self.int_to_str[0]))
                self.orientation = 0

            if right:
                # Rotates to the right. That is, adding 1
                self.orientation += 1

                if self.orientation >= len(self.int_to_str):
                    self.orientation = 0

            else:
                # Rotates to the left. That is, subtracting 1
                self.orientation -= 1

                if self.orientation < 0:
                    self.orientation = len(self.int_to_str) - 1

        except TypeError:
            print("ERROR while rotating : Invalid orientation '{}'".format(self.orientation))
            print("Recalibrating to '{}' ...".format(self.int_to_str[0]))
            self.orientation = 0

    def rotate_right(self):
        """
            Modifies the current orientation 90 degrees to the right.

        :return: None
        """
        return self.rotate(right=True)

    def rotate_left(self):
        """
            Modifies the current orientation 90 degrees to the left.

        :return: None
        """
        return self.rotate(right=False)
