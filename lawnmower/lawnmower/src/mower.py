from lawnmower.src.lawn import Lawn
from lawnmower.src.orientation import Orientation


class Mower:
    """
        A Mower.
    """
    # Mower Instruction Set
    instructions = [
        "L",    # Left Rotate (changes current orientation 90 degrees to the left)
        "R",    # Right Rotate (changes current orientation 90 degrees to the right)
        "F"     # Forward (moves 1 position in the current orientation)
    ]

    def __init__(self, x, y, orientation, lawn):
        """
            Initializes the orientation.

        :param x: (int/str) Coordinate X of the initial position of the mower in the lawn.
        :param y: (int/str) Coordinate Y of the initial position of the mower in the lawn.
        :param orientation: (lawnmower.src.orientation.Orientation) Initial orientation of the mower.
        :param lawn: (lawnmower.src.lawn.Lawn) The lawn on which it is located the mower.
        :return: None
        """
        # Coordinate X of the current position of the mower in the lawn (int)
        self.x = None

        # Coordinate Y of the current position of the mower in the lawn (int)
        self.y = None

        # Current mower orientation (instance of lawnmower.src.orientation.Orientation)
        self.orientation = None

        # The lawn on which it is located the mower (instance of lawnmower.src.lawn.Lawn)
        self.lawn = None

        try:
            if lawn.is_within(x, y):
                self.x = int(x)
                self.y = int(y)
                self.orientation = orientation
                self.lawn = lawn

            else:
                print("ERROR while initializing Mower : The specified initial position ({}, {}) is outside the "
                      "Lawn '{}'".format(x, y, lawn))

        except AttributeError:
            print("ERROR while initializing Mower : Invalid lawn '{}'".format(lawn))

    def is_properly_initialized(self):
        """
            Tells if the mower has already been properly initialized.

        :return: (bool) True if the mower has been properly initialized; False otherwise.
        """
        return isinstance(self.x, int) and isinstance(self.y, int) and isinstance(self.orientation, Orientation) and \
               isinstance(self.lawn, Lawn)                                                               # noqa : E127

    def rotate_left(self, dry_run_mode=False):
        """
            Rotates 90 degrees to the left.
        """
        if not dry_run_mode:
            # Only do something if not in dry_run mode. Orientation changes do not need to be predicted/checked.
            self.orientation.rotate_left()

    def rotate_right(self, dry_run_mode=False):
        """
            Rotates 90 degrees to the right.
        """
        if not dry_run_mode:
            # Only do something if not in dry_run mode. Orientation changes do not need to be predicted/checked.
            self.orientation.rotate_right()

    def get_forward_position_modification(self, dry_run_mode=False):
        """
            Gets the position modification if a forward instruction is going to be executed, according to current
            mower orientation and lawn info.

            IMPLEMENTATION NOTE: For improved readability reasons, in order to reduce forward method length.

        :throws AttributeError, TypeError

        :param dry_run_mode: (bool) Activates/Deactivates dry_run_mode, that allows to predict the expected new position
                            of the mower if the specified instruction were executed.

        :return: (tuple)    (x, y)

                with:
                        x : (int) Coordinate X of the mower new/predicted position
                        y : (int) Coordinate Y of the mower new/predicted position
        """
        new_x = int(self.x)
        new_y = int(self.y)

        if self.orientation.get_str() == "N":
            new_y += 1

        elif self.orientation.get_str() == "E":
            new_x += 1

        elif self.orientation.get_str() == "S":
            new_y -= 1

        elif self.orientation.get_str() == "W":
            new_x -= 1

        else:
            print("ERROR while executing forward instruction (dry_mode={}) : Unknown mower orientation '{}'".format(
                dry_run_mode, self.orientation.get_str()))

        return new_x, new_y

    def forward(self, dry_run_mode=False):
        """
            Moves 1 position forward, according to current orientation.

        :param dry_run_mode: (bool) Activates/Deactivates dry_run_mode, that allows to predict the expected new position
                            of the mower if the specified instruction were executed.

        :return: (tuple)    (x, y)

                with:
                        x : (int) Coordinate X of the mower new/predicted position
                        y : (int) Coordinate Y of the mower new/predicted position
        """
        new_x = self.x
        new_y = self.y
        error_or_outside = False

        try:
            new_x, new_y = self.get_forward_position_modification(dry_run_mode=dry_run_mode)

            # Check new position is either within or outside the lawn
            try:
                if not self.lawn.is_within(new_x, new_y):
                    # This movement leads the mower outside the lawn. Simply ignore it
                    error_or_outside = True

            except AttributeError:
                print("ERROR while executing forward instruction (dry_mode={}) : Missing lawn information".format(
                    dry_run_mode))

                # Without lawn information the movement must be ignored
                error_or_outside = True

        except AttributeError:
            print("ERROR while executing forward instruction (dry_mode={}) : Missing mower orientation".format(
                dry_run_mode))
            error_or_outside = True

        except TypeError:
            print("ERROR while executing forward instruction (dry_mode={}) : Invalid position (X={}, Y={})".format(
                dry_run_mode, self.x, self.y))
            error_or_outside = True

        if error_or_outside:
            try:
                # Simply ignore any position modification
                new_x = int(self.x)
                new_y = int(self.y)

            except TypeError:
                # Simply ignore it
                pass

        if not dry_run_mode:
            # Update current position
            self.x = new_x
            self.y = new_y

        return new_x, new_y

    def execute(self, instruction, dry_run_mode=False):
        """
            Executes the specified instruction. If the dry_mode is active (i.e., True) the mower does not really
            modify neither its position nor orientation, but simply returns which would be the expected new position.
            Otherwise, both the position and orientation of the mower would be updated, if proceeds, according to the
            executed instruction.

        :param instruction: (str) Instruction to be executed. RECALL that the implemented instructions are defined in
                            self.instructions.
        :param dry_run_mode: (bool) Activates/Deactivates dry_run_mode, that allows to predict the expected new position
                            of the mower if the specified instruction were executed.

        :return: (tuple)    (x, y)

                with:
                        x : (int) Coordinate X of the mower new/predicted position
                        y : (int) Coordinate Y of the mower new/predicted position
        """
        x = None
        y = None

        try:
            instruction_upper = instruction.upper()

            if instruction_upper in self.instructions:
                # Execute the instruction
                if instruction_upper == "L":
                    self.rotate_left(dry_run_mode=dry_run_mode)

                elif instruction_upper == "R":
                    self.rotate_right(dry_run_mode=dry_run_mode)

                else:
                    x, y = self.forward(dry_run_mode=dry_run_mode)

            else:
                print("ERROR while executing instruction '{}' (dry_mode={}) : Unknown instruction (Valid "
                      "instructions={})".format(instruction, dry_run_mode, self.instructions))

        except AttributeError:
            print("ERROR while executing instruction '{}' (dry_mode={}) : Invalid instruction (Valid "
                  "instructions={})".format(instruction, dry_run_mode, self.instructions))

        except TypeError:
            print("ERROR while executing instruction '{}' (dry_mode={}) : Missing/Invalid Mower Instruction Set "
                  "(instructions={})".format(instruction, dry_run_mode, self.instructions))

        return x, y
