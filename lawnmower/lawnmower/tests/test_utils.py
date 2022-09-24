from unittest import TestCase

from lawnmower.src.utils import get_bool_from_str
from lawnmower.tests.testutils import captured_output


class TestUtils(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__given_no_input_str__when_get_bool_from_str__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            input_str = None

            # When
            result = get_bool_from_str(input_str)

            # Then
            self.assertFalse(result)

    def test__given_invalid_input_str__when_get_bool_from_str__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            input_str = ["This", "should", "be", "a", "string"]

            # When
            result = get_bool_from_str(input_str)

            # Then
            self.assertFalse(result)

    def test__given_empty_input_str__when_get_bool_from_str__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            input_str = ""

            # When
            result = get_bool_from_str(input_str)

            # Then
            self.assertFalse(result)

    def test__given_unknown_input_str__when_get_bool_from_str__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            input_str = "unknown"

            # When
            result = get_bool_from_str(input_str)

            # Then
            self.assertFalse(result)

    def test__given_true_input_str__when_get_bool_from_str__then_return_true(self):

        with captured_output() as (out, err):

            # Given
            for input_str in ["t", "T", "True", "Yes", "y", "Y", "1"]:

                # When
                result = get_bool_from_str(input_str)

                # Then
                self.assertTrue(result)
