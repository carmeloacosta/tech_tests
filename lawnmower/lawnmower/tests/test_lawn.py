from unittest import TestCase

from lawnmower.src.lawn import Lawn
from lawnmower.tests.testutils import captured_output


class TestLawn(TestCase):

    def setUp(self):
        self.lawn = Lawn(5, 5)

    def tearDown(self):
        pass

    def test__given_no_inputs__when_init__then_one_cell_grid(self):

        with captured_output() as (out, err):

            # Given
            x_max = None
            y_max = None
            x_min = None
            y_min = None

            # When
            lawn = Lawn(x_max=x_max, y_max=y_max, x_min=x_min, y_min=y_min)

            # Then
            self.assertEqual(lawn.x_max, 1)     # RECALL the correction done in the case in which Xmin=Xmax=0
            self.assertEqual(lawn.y_max, 1)     # RECALL the correction done in the case in which Ymin=Ymax=0
            self.assertEqual(lawn.x_min, 0)
            self.assertEqual(lawn.y_min, 0)

    def test__given_invalid_inputs__when_init__then_one_cell_grid(self):

        with captured_output() as (out, err):

            # Given
            x_max = ["This", "should", "be", "an", "integer", "or", "string", "convertible", "to", "base10", "integer"]
            y_max = "This should be an integer or string convertible to base10 integer"
            x_min = "0xff"
            y_min = None

            # When
            lawn = Lawn(x_max=x_max, y_max=y_max, x_min=x_min, y_min=y_min)

            # Then
            self.assertEqual(lawn.x_max, 1)     # RECALL the correction done in the case in which Xmin=Xmax=0
            self.assertEqual(lawn.y_max, 1)     # RECALL the correction done in the case in which Ymin=Ymax=0
            self.assertEqual(lawn.x_min, 0)
            self.assertEqual(lawn.y_min, 0)

    def test__given_invalid_max_inputs__when_init__then_one_cell_grid(self):

        with captured_output() as (out, err):

            # Given
            x_max = ["This", "should", "be", "an", "integer", "or", "string", "convertible", "to", "base10", "integer"]
            y_max = "This should be an integer or string convertible to base10 integer"
            x_min = "0"     # RECALL that this is also valid, automatically converted to integer
            y_min = 0

            # When
            lawn = Lawn(x_max=x_max, y_max=y_max, x_min=x_min, y_min=y_min)

            # Then
            self.assertEqual(lawn.x_max, 0)     # RECALL the correction done in the case in which Xmin=Xmax=0
            self.assertEqual(lawn.y_max, 0)     # RECALL the correction done in the case in which Ymin=Ymax=0
            self.assertEqual(lawn.x_min, -1)
            self.assertEqual(lawn.y_min, -1)

    def test__given_valid_inputs__when_init__then_ok(self):

        with captured_output() as (out, err):

            # Given
            x_max = "5"
            y_max = "6"
            x_min = "0"
            y_min = 0

            # When
            lawn = Lawn(x_max=x_max, y_max=y_max, x_min=x_min, y_min=y_min)

            # Then
            self.assertEqual(lawn.x_max, 5)
            self.assertEqual(lawn.y_max, 6)
            self.assertEqual(lawn.x_min, 0)
            self.assertEqual(lawn.y_min, 0)

    def test__given_no_x_and_no_y__when_is_within__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            x = None
            y = None

            # When
            result = self.lawn.is_within(x, y)

            # Then
            self.assertFalse(result)

    def test__given_invalid_x_and_valid_y__when_is_within__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            x = "This should be an integer or string convertible to base10 integer"
            y = "3"

            # When
            result = self.lawn.is_within(x, y)

            # Then
            self.assertFalse(result)

    def test__given_valid_x_and_invalid_y__when_is_within__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            x = "3"
            y = ["This", "should", "be", "an", "integer", "or", "string", "convertible", "to", "base10", "integer"]

            # When
            result = self.lawn.is_within(x, y)

            # Then
            self.assertFalse(result)

    def test__given_valid_x_and_valid_y_not_within_grid__when_is_within__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            x = "10"
            y = -6

            # When
            result = self.lawn.is_within(x, y)

            # Then
            self.assertFalse(result)

    def test__given_valid_x_and_valid_y_not_within_grid__when_is_within__then_return_true(self):

        with captured_output() as (out, err):

            # Given
            x = "3"
            y = 3

            # When
            result = self.lawn.is_within(x, y)

            # Then
            self.assertTrue(result)

    def test__given_not_initialized__when_repr__then_ok(self):

        with captured_output() as (out, err):

            # Given
            self.lawn = Lawn(None, None)

            # When
            result = self.lawn.__repr__()

            # Then
            expected_result = "((Xmin={},Ymin={}), (Xmax={},Ymax={})".format(self.lawn.x_min, self.lawn.y_min,
                                                                             self.lawn.x_max, self.lawn.y_max)
            self.assertEqual(result, expected_result)
