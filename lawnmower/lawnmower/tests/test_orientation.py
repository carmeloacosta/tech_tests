from unittest import TestCase
from unittest.mock import patch

from lawnmower.src.orientation import Orientation
from lawnmower.tests.testutils import captured_output


class TestOrientation(TestCase):

    def setUp(self):
        self.orientation = Orientation()

    def tearDown(self):
        pass

    def test__given_orientation_0__when_whenever__then_implemented_as_north(self):

        with captured_output() as (out, err):

            # Given
            orientation = 0
            expected_orientation_str = "N"

            # When + Then
            self.assertEqual(Orientation.int_to_str[orientation], expected_orientation_str)

    def test__given_orientation_1__when_whenever__then_implemented_as_east(self):

        with captured_output() as (out, err):

            # Given
            orientation = 1
            expected_orientation_str = "E"

            # When + Then
            self.assertEqual(Orientation.int_to_str[orientation], expected_orientation_str)

    def test__given_orientation_2__when_whenever__then_implemented_as_south(self):

        with captured_output() as (out, err):

            # Given
            orientation = 2
            expected_orientation_str = "S"

            # When + Then
            self.assertEqual(Orientation.int_to_str[orientation], expected_orientation_str)

    def test__given_orientation_3__when_whenever__then_implemented_as_west(self):

        with captured_output() as (out, err):

            # Given
            orientation = 3
            expected_orientation_str = "W"

            # When + Then
            self.assertEqual(Orientation.int_to_str[orientation], expected_orientation_str)

    def test__given_whatever__when_whenever__then_only_four_orientations_implemented(self):

        with captured_output() as (out, err):

            # When + Then
            self.assertEqual(len(Orientation.int_to_str), 4)

    def test__given_orientation_str_north__when_whenever__then_implemented_as_0(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = "N"
            expected_orientation = 0

            # When + Then
            self.assertEqual(Orientation.str_to_int[orientation_str], expected_orientation)

    def test__given_orientation_str_east__when_whenever__then_implemented_as_1(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = "E"
            expected_orientation = 1

            # When + Then
            self.assertEqual(Orientation.str_to_int[orientation_str], expected_orientation)

    def test__given_orientation_str_south__when_whenever__then_implemented_as_2(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = "S"
            expected_orientation = 2

            # When + Then
            self.assertEqual(Orientation.str_to_int[orientation_str], expected_orientation)

    def test__given_orientation_str_west__when_whenever__then_implemented_as_3(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = "W"
            expected_orientation = 3

            # When + Then
            self.assertEqual(Orientation.str_to_int[orientation_str], expected_orientation)

    def test__given_whatever__when_whenever__then_only_four_str_orientations_implemented(self):

        with captured_output() as (out, err):

            # When + Then
            self.assertEqual(len(Orientation.str_to_int), 4)

    def test__given_no_orientation_str__when_init__then_default_orientation(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = None
            expected_orientation = 0

            # When
            orientation = Orientation(orientation_str)

            # Then
            self.assertEqual(orientation.orientation, expected_orientation)

    def test__given_invalid_orientation_str__when_init__then_default_orientation(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = ["This", "should", "be", "a", "string"]
            expected_orientation = 0

            # When
            orientation = Orientation(orientation_str)

            # Then
            self.assertEqual(orientation.orientation, expected_orientation)

    def test__given_unknown_orientation_str__when_init__then_default_orientation(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = "X"
            expected_orientation = 0

            # When
            orientation = Orientation(orientation_str)

            # Then
            self.assertEqual(orientation.orientation, expected_orientation)

    def test__given_valid_orientation_str__when_init__then_specified_orientation_str(self):

        with captured_output() as (out, err):

            # Given
            for orientation_str in ["N", "E", "S", "W"]:

                expected_orientation = Orientation.str_to_int[orientation_str]

                # When
                orientation = Orientation(orientation_str)

                # Then
                self.assertEqual(orientation.orientation, expected_orientation)

    def test__given_no_orientation__when_get_str__then_returns_none(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = None

            # When
            result = self.orientation.get_str()

            # Then
            self.assertIsNone(result)

    def test__given_invalid_orientation__when_get_str__then_returns_none(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = ["This", "should", "be", "an", "integer"]

            # When
            result = self.orientation.get_str()

            # Then
            self.assertIsNone(result)

    def test__given_unknown_orientation__when_get_str__then_returns_none(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = "UNKNOWN"

            # When
            result = self.orientation.get_str()

            # Then
            self.assertIsNone(result)

    def test__given_valid_orientation__when_get_str__then_ok(self):

        with captured_output() as (out, err):

            # Given
            for orientation in [0, 1, 2, 3]:

                self.orientation.orientation = orientation
                expected_orientation_str = Orientation.int_to_str[orientation]

                # When
                result = self.orientation.get_str()

                # Then
                self.assertEqual(result, expected_orientation_str)

    def test__given_no_orientation__when_set__then_nothing_happens(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = None

            # When
            self.orientation.set(orientation_str)

            # Then
            self.assertEqual(self.orientation.orientation, 0)   # That is, the same value remains unmodified

    def test__given_invalid_orientation__when_set__then_nothing_happens(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = ["This", "should", "be", "an", "integer"]

            # When
            self.orientation.set(orientation_str)

            # Then
            self.assertEqual(self.orientation.orientation, 0)   # That is, the same value remains unmodified

    def test__given_unknown_orientation__when_set__then_nothing_happens(self):

        with captured_output() as (out, err):

            # Given
            orientation_str = "UNKNOWN"

            # When
            self.orientation.set(orientation_str)

            # Then
            self.assertEqual(self.orientation.orientation, 0)   # That is, the same value remains unmodified

    def test__given_valid_orientation__when_set__then_ok(self):

        with captured_output() as (out, err):

            # Given

            # Let's set this to an invalid value just to notice that all valid values are properly set
            self.orientation.orientation = None

            for orientation_str in Orientation.str_to_int:

                expected_orientation = Orientation.str_to_int[orientation_str]

                # When
                self.orientation.set(orientation_str)

                # Then
                self.assertEqual(self.orientation.orientation, expected_orientation)

    def test__given_no_orientation_and_no_right__when_rotate__then_default_orientation(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = None

            # When
            self.orientation.rotate(right=None)

            # Then
            self.assertEqual(self.orientation.orientation, 0)

    def test__given_invalid_orientation_and_no_right__when_rotate__then_default_orientation(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = ["This", "should", "be", "an", "integer"]

            # When
            self.orientation.rotate(right=None)

            # Then
            self.assertEqual(self.orientation.orientation, 0)

    def test__given_invalid_str_orientation_and_no_right__when_rotate__then_default_orientation(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = "100"

            # When
            self.orientation.rotate(right=None)

            # Then
            self.assertEqual(self.orientation.orientation, 0)

    def test__given_orientation_overflow_and_no_right__when_rotate__then_ok(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = 100
            expected_orientation = len(Orientation.int_to_str) - 1  # RECALL that first it is recalibrated

            # When
            self.orientation.rotate(right=None)

            # Then
            self.assertEqual(self.orientation.orientation, expected_orientation)

    def test__given_orientation_underflow_and_no_right__when_rotate__then_ok(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = -50
            expected_orientation = len(Orientation.int_to_str) - 1  # RECALL that first it is recalibrated

            # When
            self.orientation.rotate(right=None)

            # Then
            self.assertEqual(self.orientation.orientation, expected_orientation)

    def test__given_orientation_overflow_and_right__when_rotate__then_ok(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = 100
            expected_orientation = 1  # RECALL that first it is recalibrated

            # When
            self.orientation.rotate(right=True)

            # Then
            self.assertEqual(self.orientation.orientation, expected_orientation)

    def test__given_orientation_underflow_and_right__when_rotate__then_ok(self):

        with captured_output() as (out, err):

            # Given
            self.orientation.orientation = -50
            expected_orientation = 1  # RECALL that first it is recalibrated

            # When
            self.orientation.rotate(right=True)

            # Then
            self.assertEqual(self.orientation.orientation, expected_orientation)

    def test__given_valid_orientation_and_no_right__when_rotate__then_ok(self):

        with captured_output() as (out, err):

            # Given
            for orientation in Orientation.int_to_str:

                self.orientation.orientation = orientation
                expected_orientation = orientation - 1

                if expected_orientation < 0:
                    expected_orientation = len(Orientation.int_to_str) - 1

                # When
                self.orientation.rotate(right=None)

                # Then
                self.assertEqual(self.orientation.orientation, expected_orientation)

    def test__given_valid_orientation_and_right__when_rotate__then_ok(self):

        with captured_output() as (out, err):

            # Given
            for orientation in Orientation.int_to_str:

                self.orientation.orientation = orientation
                expected_orientation = orientation + 1

                if expected_orientation >= len(Orientation.int_to_str):
                    expected_orientation = 0

                # When
                self.orientation.rotate(right=True)

                # Then
                self.assertEqual(self.orientation.orientation, expected_orientation)

    @patch("lawnmower.src.orientation.Orientation.rotate")
    def test__given_whatever__when_rotate_right__then_ok(self, rotate_mock):

        with captured_output() as (out, err):

            # When
            self.orientation.rotate_right()

            # Then
            rotate_mock.assert_called_once_with(right=True)

    @patch("lawnmower.src.orientation.Orientation.rotate")
    def test__given_whatever__when_rotate_left__then_ok(self, rotate_mock):

        with captured_output() as (out, err):

            # When
            self.orientation.rotate_left()

            # Then
            rotate_mock.assert_called_once_with(right=False)
