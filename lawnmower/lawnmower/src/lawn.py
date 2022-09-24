class Lawn:
    """
        Rectangular Lawn.

        It is divided into a grid to simplify the navigation. The coordinates of each cell of the grid are the
        following:

                       ___________________ ______________________ ...    _____________________
                      | (x_min, y_max)   | (x_min + 1, y_max)   | ...   |  (x_max, y_max)    |
                      ____________________ ______________________ ...   ______________________
                      | (x_min, y_max-1) | (x_min + 1, y_max-1) | ...   |  (x_max, y_max-1)  |
                      ____________________ ______________________ ...   ______________________
                      ...              ...            ...    ...
                      ____________________ ______________________ ...   ______________________
                      | (x_min, 0)       | (x_min + 1, 0)       | ...   |  (x_max, 0)        |
                      ____________________ ______________________ ...   ______________________

        If not specified (optional), the bottom-left corner of the grid is (0, 0). That is, x_min = 0 and y_min = 0.

                       _______________ ______________ ...    _____________________
                      | (0, y_max)   | (1, y_max)   | ...   |  (x_max, y_max)    |
                      ________________ ______________ ...    ____________________
                      | (0, y_max-1) | (1, y_max-1) | ...   |  (x_max, y_max-1) |
                      ________________ ______________ ...    ____________________
                      ...              ...            ...    ...
                      ________________ ______________ ...    ____________________
                      | (0, 0)       | (1, 0)       | ...   |  (x_max, 0)       |
                      ________________ ______________ ...    ____________________


        The cell directly at North of the position (x, y) has for coordinates (x, y+1).
        Therefore, this is the grid orientation:

                                                North
                                                  ^
                                                  |
                                              _________
                                   West < -  | (x, y) | - >  East
                                             _________
                                                 |
                                               South
    """
    def __init__(self, x_max, y_max, x_min=0, y_min=0):
        # Coordinate X of the upper-right corner of the grid
        try:
            self.x_max = int(x_max)

        except (ValueError, TypeError):
            print("ERROR while initializing Lawn : Invalid Xmax coordinate '{}'".format(x_max))
            print("Setting Xmax to 0 ...")
            self.x_max = 0

        # Coordinate Y of the upper-right corner of the grid
        try:
            self.y_max = int(y_max)

        except (ValueError, TypeError):
            print("ERROR while initializing Lawn : Invalid Ymax coordinate '{}'".format(y_max))
            print("Setting Ymax to 0 ...")
            self.y_max = 0

        # Coordinate X of the lower-left corner of the grid
        try:
            self.x_min = int(x_min)
            if self.x_min >= self.x_max:
                print("ERROR while initializing Lawn : Invalid Xmin coordinate '{}'. Must be lower than Xmax "
                      "(Xmax={})".format(x_min, self.x_max))
                print("Setting Xmin to '{}' (Xmax-1) ...".format(self.x_max - 1))
                self.x_min = self.x_max - 1

        except (ValueError, TypeError):
            print("ERROR while initializing Lawn : Invalid Xmin coordinate '{}'".format(x_min))
            print("Setting Xmin to 0 ...")
            self.x_min = 0

        # Coordinate Y of the lower-left corner of the grid
        try:
            self.y_min = int(y_min)
            if self.y_min >= self.y_max:
                print("ERROR while initializing Lawn : Invalid Ymin coordinate '{}'. Must be lower than Ymax "
                      "(Ymax={})".format(y_min, self.y_max))
                print("Setting Ymin to '{}' (Ymax-1) ...".format(self.y_max - 1))
                self.y_min = self.y_max - 1

        except (ValueError, TypeError):
            print("ERROR while initializing Lawn : Invalid Ymin coordinate '{}'".format(y_min))
            print("Setting Ymin to 0 ...")
            self.y_min = 0

        # Consider the case in which Xmin=Xmax=0
        if self.x_max == 0 and self.x_min == 0:
            print("ERROR while initializing Lawn : Xmin and Xmax coordinates are zero")
            print("Setting Xmax to 1 ...")
            self.x_max = 1

        # Consider the case in which Ymin=Ymax=0
        if self.y_max == 0 and self.y_min == 0:
            print("ERROR while initializing Lawn : Ymin and Ymax coordinates are zero")
            print("Setting Ymax to 1 ...")
            self.y_max = 1

    def is_within(self, x, y):
        """
            Given a cell of the lawn grid, specified by (x,y) coordinates, returns True if the cell is within the grid.
            That is, returns True if the position (x,y) is a valid position in the lawn.

        :param x: (int) Coordinate in the X Axis of the cell to check.
        :param y: (int) Coordinate in the Y Axis of the cell to check.
        :return: (bool) True if the cell checked is a valid one, contained in the lawn.
        """
        try:
            x_int = int(x)

        except (ValueError, TypeError):
            print("ERROR while checking if is_withing Lawn : Invalid X coordinate '{}'".format(x))
            return False

        try:
            y_int = int(y)

        except (ValueError, TypeError):
            print("ERROR while checking if is_withing Lawn : Invalid Y coordinate '{}'".format(y))
            return False

        return self.x_min <= x_int <= self.x_max and self.y_min <= y_int <= self.y_max

    def __repr__(self):
        return "((Xmin={},Ymin={}), (Xmax={},Ymax={})".format(self.x_min, self.y_min, self.x_max, self.y_max)
