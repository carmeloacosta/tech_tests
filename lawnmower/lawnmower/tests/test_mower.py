from unittest import TestCase
from unittest.mock import patch, Mock

import lawnmower.src.lawn
from lawnmower.src.mower import Mower
from lawnmower.tests.testutils import captured_output
from lawnmower.tests.mocks.lawn_mock import LawnMock
from lawnmower.tests.mocks.orientation_mock import OrientationMock


class TestMower(TestCase):

    def setUp(self):

        with captured_output() as (out, err):
            self.lawn_mock = LawnMock()
            self.orientation_mock = OrientationMock()
            self.mower = Mower("3", "2", self.orientation_mock, self.lawn_mock)

    def tearDown(self):
        pass

    def test__given_instruction_l_lower__when_whenever__then_not_implemented(self):

        with captured_output() as (out, err):

            # Given
            instruction = "l"

            # When + Then
            self.assertFalse(instruction in Mower.instructions)

    def test__given_instruction_r_lower__when_whenever__then_not_implemented(self):

        with captured_output() as (out, err):

            # Given
            instruction = "r"

            # When + Then
            self.assertFalse(instruction in Mower.instructions)

    def test__given_instruction_f_lower__when_whenever__then_not_implemented(self):

        with captured_output() as (out, err):

            # Given
            instruction = "f"

            # When + Then
            self.assertFalse(instruction in Mower.instructions)

    def test__given_instruction_l_upper__when_whenever__then_implemented(self):

        with captured_output() as (out, err):

            # Given
            instruction = "L"

            # When + Then
            self.assertTrue(instruction in Mower.instructions)

    def test__given_instruction_r_upper__when_whenever__then_implemented(self):

        with captured_output() as (out, err):

            # Given
            instruction = "R"

            # When + Then
            self.assertTrue(instruction in Mower.instructions)

    def test__given_instruction_f_upper__when_whenever__then_implemented(self):

        with captured_output() as (out, err):

            # Given
            instruction = "F"

            # When + Then
            self.assertTrue(instruction in Mower.instructions)

    def test__given_whatever__when_whenever__then_three_instructions_implemented(self):

        with captured_output() as (out, err):

            # When + Then
            self.assertEqual(len(Mower.instructions), 3)

    def test__given_no_x_and_no_y_and_no_orientation_and_no_lawn__when_init__then_all_none(self):

        with captured_output() as (out, err):

            # Given
            x = None
            y = None
            orientation = None
            lawn = None

            # When
            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # Then
            self.assertIsNone(self.mower.x)
            self.assertIsNone(self.mower.y)
            self.assertIsNone(self.mower.orientation)
            self.assertIsNone(self.mower.lawn)

    def test__given_valid_x_and_valid_y_and_no_orientation_and_no_lawn__when_init__then_all_none(self):

        with captured_output() as (out, err):

            # Given
            x = "3"     # RECALL that, besides being valid, the mower must be within the lawn
            y = "2"     # RECALL that, besides being valid, the mower must be within the lawn
            orientation = None
            lawn = None

            # When
            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # Then
            self.assertIsNone(self.mower.x)
            self.assertIsNone(self.mower.y)
            self.assertIsNone(self.mower.orientation)
            self.assertIsNone(self.mower.lawn)

    def test__given_valid_x_and_valid_y_and_no_orientation_and_valid_lawn__when_init__then_ok(self):

        with captured_output() as (out, err):

            # Given
            x = "3"
            y = "2"
            orientation = None
            lawn = LawnMock(expected_is_within_response=True)

            # When
            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # Then
            self.assertEqual(self.mower.x, int(x))
            self.assertEqual(self.mower.y, int(y))
            self.assertIsNone(self.mower.orientation)
            self.assertEqual(self.mower.lawn, lawn)

    def test__given_valid_x_and_valid_y_and_valid_orientation_and_valid_lawn__when_init__then_ok(self):

        with captured_output() as (out, err):

            # Given
            x = "3"
            y = "2"
            orientation = OrientationMock()
            lawn = LawnMock(expected_is_within_response=True)

            # When
            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # Then
            self.assertEqual(self.mower.x, int(x))
            self.assertEqual(self.mower.y, int(y))
            self.assertEqual(self.mower.orientation, orientation)
            self.assertEqual(self.mower.lawn, lawn)

    def test__given_no_x_and_no_y_and_no_orientation_and_no_lawn__when_is_properly_initialized__then_false(self):

        with captured_output() as (out, err):

            # Given
            x = None
            y = None
            orientation = None
            lawn = None

            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # When
            result = self.mower.is_properly_initialized()

            # Then
            self.assertFalse(result)

    def test__given_valid_x_and_valid_y_and_no_orientation_and_no_lawn__when_is_properly_initialized__then_false(self):

        with captured_output() as (out, err):

            # Given
            x = "3"     # RECALL that, besides being valid, the mower must be within the lawn
            y = "2"     # RECALL that, besides being valid, the mower must be within the lawn
            orientation = None
            lawn = None

            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # When
            result = self.mower.is_properly_initialized()

            # Then
            self.assertFalse(result)

    def test__given_valid_x_and_valid_y_and_no_orientation_and_valid_lawn__when_is_properly_initialized__then_false(
            self):

        with captured_output() as (out, err):

            # Given
            x = "3"
            y = "2"
            orientation = None
            lawn = Mock(spec=lawnmower.src.lawn.Lawn)       # Properly mocks Lawn, even at isinstance level
            lawn.is_within.return_value = True              # Properly mocks lawn.is_within

            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # When
            result = self.mower.is_properly_initialized()

            # Then
            self.assertFalse(result)

    def test__given_valid_x_and_valid_y_and_valid_orientation_and_valid_lawn__when_is_properly_initialized__then_true(
            self):

        with captured_output() as (out, err):

            # Given
            x = "3"
            y = "2"
            orientation = Mock(spec=lawnmower.src.orientation.Orientation)  # Properly mocks Orientation
            lawn = Mock(spec=lawnmower.src.lawn.Lawn)       # Properly mocks Lawn, even at isinstance level
            lawn.is_within.return_value = True              # Mocks lawn.is_within

            self.mower = Mower(x=x, y=y, orientation=orientation, lawn=lawn)

            # When
            result = self.mower.is_properly_initialized()

            # Then
            self.assertTrue(result)

    def test__given_not_dry_run_mode__when_rotate_left__then_orientation_rotate_left_called(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False
            self.mower.orientation = Mock()

            # When
            self.mower.rotate_left(dry_run_mode=dry_run_mode)

            # Then
            self.mower.orientation.rotate_left.assert_called_once_with()

    def test__given_dry_run_mode__when_rotate_left__then_orientation_rotate_left_not_called(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = True
            self.mower.orientation = Mock()

            # When
            self.mower.rotate_left(dry_run_mode=dry_run_mode)

            # Then
            self.mower.orientation.rotate_left.assert_not_called()

    def test__given_not_dry_run_mode__when_rotate_right__then_orientation_rotate_right_called(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False
            self.mower.orientation = Mock()

            # When
            self.mower.rotate_right(dry_run_mode=dry_run_mode)

            # Then
            self.mower.orientation.rotate_right.assert_called_once_with()

    def test__given_dry_run_mode__when_rotate_right__then_orientation_rotate_right_not_called(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = True
            self.mower.orientation = Mock()

            # When
            self.mower.rotate_right(dry_run_mode=dry_run_mode)

            # Then
            self.mower.orientation.rotate_right.assert_not_called()

    def test__given_not_dry_run_mode_and_no_x_no_y_no_orientation_no_lawn__when_forward__then_return_none_none(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            self.mower.x = None
            self.mower.y = None
            self.mower.orientation = None
            self.mower.lawn = None

            expected_result = (None, None)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_no_x_no_y_and_valid_orientation_no_lawn__when_forward__then_return_none_none(
            self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            self.mower.x = None
            self.mower.y = None

            for expected_orientation_str in ["N", "E", "S", "W"]:

                orientation_mock = Mock()
                orientation_mock.get_str.return_value = expected_orientation_str
                self.mower.orientation = orientation_mock

                self.mower.lawn = None

                expected_result = (None, None)

                # When
                result = self.mower.forward(dry_run_mode=dry_run_mode)

                # Then
                self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_x_y_and_no_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            self.mower.orientation = None

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has NOT been updated
            self.assertEqual(self.mower.x, expected_x)
            self.assertEqual(self.mower.y, expected_y)

    def test__given_not_dry_run_mode_and_x_y_and_north_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "N"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x, expected_y + 1)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has been updated
            self.assertEqual(self.mower.x, expected_x)
            self.assertEqual(self.mower.y, expected_y + 1)

    def test__given_not_dry_run_mode_and_x_y_and_east_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "E"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x + 1, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has been updated
            self.assertEqual(self.mower.x, expected_x + 1)
            self.assertEqual(self.mower.y, expected_y)

    def test__given_not_dry_run_mode_and_x_y_and_south_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "S"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x, expected_y - 1)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has been updated
            self.assertEqual(self.mower.x, expected_x)
            self.assertEqual(self.mower.y, expected_y - 1)

    def test__given_not_dry_run_mode_and_x_y_and_west_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "W"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x - 1, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has been updated
            self.assertEqual(self.mower.x, expected_x - 1)
            self.assertEqual(self.mower.y, expected_y)

    def test__given_dry_run_mode_and_x_y_and_north_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = True

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "N"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x, expected_y + 1)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has NOT been updated
            self.assertEqual(self.mower.x, str(expected_x))
            self.assertEqual(self.mower.y, str(expected_y))

    def test__given_dry_run_mode_and_x_y_and_east_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = True

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "E"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x + 1, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has NOT been updated
            self.assertEqual(self.mower.x, str(expected_x))
            self.assertEqual(self.mower.y, str(expected_y))

    def test__given_dry_run_mode_and_x_y_and_south_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = True

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "S"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x, expected_y - 1)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has NOT been updated
            self.assertEqual(self.mower.x, str(expected_x))
            self.assertEqual(self.mower.y, str(expected_y))

    def test__given_dry_run_mode_and_x_y_and_west_orientation_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = True

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "W"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x - 1, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

            # Check that mower position has NOT been updated
            self.assertEqual(self.mower.x, str(expected_x))
            self.assertEqual(self.mower.y, str(expected_y))

    def test__given_not_dry_run_mode_and_x_y_and_north_orientation_not_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "N"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = False
            self.mower.lawn = lawn_mock

            # RECALL that if the position after the move is outside the lawn, then the mower do not move, it keeps its
            # orientation
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_x_y_and_east_orientation_not_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "E"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = False
            self.mower.lawn = lawn_mock

            # RECALL that if the position after the move is outside the lawn, then the mower do not move, it keeps its
            # orientation
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_x_y_and_south_orientation_not_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "S"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = False
            self.mower.lawn = lawn_mock

            # RECALL that if the position after the move is outside the lawn, then the mower do not move, it keeps its
            # orientation
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_x_y_and_west_orientation_not_within_lawn__when_forward__then_ok(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "W"
            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = False
            self.mower.lawn = lawn_mock

            # RECALL that if the position after the move is outside the lawn, then the mower do not move, it keeps its
            # orientation
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_x_y_and_valid_orientation_no_lawn__when_forward__then_return_none_none(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            for expected_orientation_str in ["N", "E", "S", "W"]:

                orientation_mock = Mock()
                orientation_mock.get_str.return_value = expected_orientation_str
                self.mower.orientation = orientation_mock

                self.mower.lawn = None

                expected_result = (expected_x, expected_y)

                # When
                result = self.mower.forward(dry_run_mode=dry_run_mode)

                # Then
                self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_x_y_and_unknown_orientation_no_lawn__when_forward__then_same_x_y(self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "UNKNOWN"

            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            self.mower.lawn = None

            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_not_dry_run_mode_and_x_y_and_unknown_orientation_within_lawn__when_forward__then_return_same_x_y(
            self):

        with captured_output() as (out, err):

            # Given
            dry_run_mode = False

            expected_x = 3
            expected_y = 2

            self.mower.x = str(expected_x)
            self.mower.y = str(expected_y)

            expected_orientation_str = "UNKNOWN"

            orientation_mock = Mock()
            orientation_mock.get_str.return_value = expected_orientation_str
            self.mower.orientation = orientation_mock

            lawn_mock = Mock()
            lawn_mock.is_within.return_value = True
            self.mower.lawn = lawn_mock

            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.forward(dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_no_instruction_no_dry_run_mode_no_implemented_instructions__when_execute__then_return_none_none(
            self):

        with captured_output() as (out, err):

            # Given
            instruction = None
            dry_run_mode = False

            self.mower.instructions = None

            expected_x = None
            expected_y = None
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_invalid_instruction_no_dry_run_mode_no_implemented_instructions__when_execute__then_ret_none_none(
            self):

        with captured_output() as (out, err):

            # Given
            instruction = ["This", "should", "be", "a", "string"]
            dry_run_mode = False

            self.mower.instructions = None

            expected_x = None
            expected_y = None
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_unknown_instruction_no_dry_run_mode_no_implemented_instructions__when_execute__then_ret_none_none(
            self):

        with captured_output() as (out, err):

            # Given
            instruction = "unknown"
            dry_run_mode = False

            self.mower.instructions = None

            expected_x = None
            expected_y = None
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_unknown_instruction_no_dry_run_mode_invalid_implemented_instructions__when_execute__then_none_none(
            self):

        with captured_output() as (out, err):

            # Given
            instruction = "unknown"
            dry_run_mode = False

            self.mower.instructions = 101  # RECALL that this must be a list of implemented instruction names

            expected_x = None
            expected_y = None
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    def test__given_unknown_instruction_no_dry_run_mode_valid_implemented_instructions__when_execute__then_none_none(
            self):

        with captured_output() as (out, err):

            # Given
            instruction = "unknown"
            dry_run_mode = False

            expected_x = None
            expected_y = None
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)

    @patch("lawnmower.src.mower.Mower.forward")
    @patch("lawnmower.src.mower.Mower.rotate_right")
    @patch("lawnmower.src.mower.Mower.rotate_left")
    def test__given_rotate_left_instruction_no_dry_run_mode_valid_implemented_instructions__when_execute__then_ok(
            self, rotate_left_mock, rotate_right_mock, forward_mock):

        with captured_output() as (out, err):

            # Given
            instruction = "l"
            dry_run_mode = False

            expected_x = None
            expected_y = None
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)
            rotate_left_mock.assert_called_once_with(dry_run_mode=dry_run_mode)
            rotate_right_mock.assert_not_called()
            forward_mock.assert_not_called()

    @patch("lawnmower.src.mower.Mower.forward")
    @patch("lawnmower.src.mower.Mower.rotate_right")
    @patch("lawnmower.src.mower.Mower.rotate_left")
    def test__given_rotate_right_instruction_no_dry_run_mode_valid_implemented_instructions__when_execute__then_ok(
            self, rotate_left_mock, rotate_right_mock, forward_mock):

        with captured_output() as (out, err):

            # Given
            instruction = "r"
            dry_run_mode = False

            expected_x = None
            expected_y = None
            expected_result = (expected_x, expected_y)

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)
            rotate_left_mock.assert_not_called()
            rotate_right_mock.assert_called_once_with(dry_run_mode=dry_run_mode)
            forward_mock.assert_not_called()

    @patch("lawnmower.src.mower.Mower.forward")
    @patch("lawnmower.src.mower.Mower.rotate_right")
    @patch("lawnmower.src.mower.Mower.rotate_left")
    def test__given_forward_instruction_no_dry_run_mode_valid_implemented_instructions__when_execute__then_ok(
            self, rotate_left_mock, rotate_right_mock, forward_mock):

        with captured_output() as (out, err):

            # Given
            instruction = "f"
            dry_run_mode = False

            expected_result = (3, 3)
            forward_mock.return_value = expected_result

            # When
            result = self.mower.execute(instruction=instruction, dry_run_mode=dry_run_mode)

            # Then
            self.assertTupleEqual(result, expected_result)
            rotate_left_mock.assert_not_called()
            rotate_right_mock.assert_not_called()
            forward_mock.assert_called_once_with(dry_run_mode=dry_run_mode)
