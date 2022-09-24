from unittest import TestCase
from unittest.mock import patch
from os.path import join

from lawnmower.src.config_file import ConfigFile
from lawnmower.tests.testutils import captured_output, get_fixtures_path


class TestConfigFile(TestCase):

    def setUp(self):
        self.config_file = ConfigFile()
        self.fixture_path = join(get_fixtures_path(), "config_file")

    def tearDown(self):
        pass

    def test__given_whatever__when_init__then_ok(self):

        with captured_output() as (out, err):

            # When
            self.config_file = ConfigFile()

            # Then
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_no_file__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = None

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_invalid_file__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = ["This", "must", "be", "a", "string"]

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_missing_file__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "missing_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    @patch("lawnmower.src.config_file.ConfigFile.open_file")
    def test__given_unexpected_error__when_load__then_return_false(self, open_file_mock):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "unexpected_error.txt")

            open_file_mock.side_effect = Exception("Unexpected error")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_empty_file__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "empty_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_incomplete_first_line__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "only_x_max_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_only_valid_first_line__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "only_first_line_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_only_two_valid_lines__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "only_first_two_lines_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_single_mower_info__when_load__then_return_true(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "single_mower_info_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertTrue(result)

            # Check that it WAS updated
            expected_mower_info = {
                "initial_position": ("1", "2"),
                "initial_orientation": "N",
                "instruction_list": "LFLFLFLFF"
            }
            self.assertEqual(self.config_file.lawn_x_max, '5')
            self.assertEqual(self.config_file.lawn_y_max, '6')
            self.assertEqual(len(self.config_file.mowers), 1)
            self.assertDictEqual(self.config_file.mowers[0], expected_mower_info)

    def test__given_multi_mower_info_second_mower_position_error__when_load__then_return_false(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "multi_mower_info_error_in_second_mower_position_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            self.assertFalse(result)

            # Check that it was NOT updated
            self.assertIsNone(self.config_file.lawn_x_max)
            self.assertIsNone(self.config_file.lawn_y_max)
            self.assertListEqual(self.config_file.mowers, [])

    def test__given_multi_mower_info_second_mower_instructions_error__when_load__then_return_true(self):

        with captured_output() as (out, err):

            # Given
            filepath = join(self.fixture_path, "multi_mower_info_error_in_second_mower_instructions_file.txt")

            # When
            result = self.config_file.load(filepath)

            # Then
            # NOTICE that it does NOT check the instruction list. It will proceed and fail when executing the
            # corresponding mower instructions.
            self.assertTrue(result)

            # Check that it WAS updated
            expected_mower_1_info = {
                "initial_position": ("1", "2"),
                "initial_orientation": "N",
                "instruction_list": "LFLFLFLFF"
            }

            expected_mower_2_info = {
                "initial_position": ("3", "3"),
                "initial_orientation": "E",
                "instruction_list": "LFLFL 2 3 E RRFFFLLR"      # This is the instruction list including the error
            }

            self.assertEqual(self.config_file.lawn_x_max, '5')
            self.assertEqual(self.config_file.lawn_y_max, '6')
            self.assertEqual(len(self.config_file.mowers), 2)
            self.assertDictEqual(self.config_file.mowers[0], expected_mower_1_info)
            self.assertDictEqual(self.config_file.mowers[1], expected_mower_2_info)
