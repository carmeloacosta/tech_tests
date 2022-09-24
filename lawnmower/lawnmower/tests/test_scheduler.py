from unittest import TestCase
from unittest.mock import patch, call, Mock

from lawnmower.src.scheduler import Scheduler
from lawnmower.tests.testutils import captured_output


class TestScheduler(TestCase):

    def setUp(self):
        self.scheduler = Scheduler(None)

    def tearDown(self):
        pass

    def test__given_no_config_file_and_no_mower_overlapping__when_init__then_ok(self):

        with captured_output() as (out, err):

            # Given
            config_file = None
            mower_overlapping = None

            # When
            self.scheduler = Scheduler(config_file=config_file, mower_overlapping=mower_overlapping)

            # Then
            self.assertEqual(self.scheduler.config_file, config_file)
            self.assertEqual(self.scheduler.mower_overlapping, mower_overlapping)
            self.assertIsNone(self.scheduler.lawn)
            self.assertListEqual(self.scheduler.mowers, [])

    def test__given_config_file_and_mower_overlapping__when_init__then_ok(self):

        with captured_output() as (out, err):

            # Given
            config_file = Mock()
            mower_overlapping = True

            # When
            self.scheduler = Scheduler(config_file=config_file, mower_overlapping=mower_overlapping)

            # Then
            self.assertEqual(self.scheduler.config_file, config_file)
            self.assertEqual(self.scheduler.mower_overlapping, mower_overlapping)
            self.assertIsNone(self.scheduler.lawn)
            self.assertListEqual(self.scheduler.mowers, [])

    def test__given_no_mowers__when_repr__then_empty_result(self):

        with captured_output() as (out, err):

            # Given
            self.scheduler.mowers = None

            # When
            result = self.scheduler.__repr__()

            # Then
            self.assertEqual(result, "")

    def test__given_invalid_mowers__when_repr__then_empty_result(self):

        with captured_output() as (out, err):

            # Given
            self.scheduler.mowers = 10

            # When
            result = self.scheduler.__repr__()

            # Then
            self.assertEqual(result, "")

    def test__given_empty_mowers__when_repr__then_empty_result(self):

        with captured_output() as (out, err):

            # Given
            self.scheduler.mowers = []

            # When
            result = self.scheduler.__repr__()

            # Then
            self.assertEqual(result, "")
            self.assertEqual(len(self.scheduler.mowers), 0)

    def test__given_list_of_invalid_mowers__when_repr__then_empty_result(self):

        with captured_output() as (out, err):

            # Given
            self.scheduler.mowers = ["mower1", "mower2"]

            # When
            result = self.scheduler.__repr__()

            # Then
            self.assertEqual(result, "")

    def test__given_list_of_valid_mowers__when_repr__then_ok(self):

        with captured_output() as (out, err):

            # Given
            mower1_mock = Mock()
            mower1_mock.x = 1
            mower1_mock.y = 2
            mower1_mock.orientation = Mock()
            mower1_mock.orientation.get_str.return_value = "N"

            mower2_mock = Mock()
            mower2_mock.x = 3
            mower2_mock.y = 4
            mower2_mock.orientation = Mock()
            mower2_mock.orientation.get_str.return_value = "E"

            self.scheduler.mowers = [mower1_mock, mower2_mock]

            # When
            result = self.scheduler.__repr__()

            # Then
            expected_result = "1 2 N\n3 4 E\n"
            self.assertEqual(result, expected_result)
            self.assertEqual(len(self.scheduler.mowers), 2)

    def test__given_message__when_print__then_ok(self):

        with captured_output() as (out, err):

            # Given
            for message in [None, ["whatever", "message", "works"], "although a string would be adequate"]:

                # When
                self.scheduler.print(message)

                # Then
                # Simply check the test output without capturing it (i.e., captured_output(False))

    def test__given_no_config_file__when_run__then_nothing_happens(self):

        with captured_output() as (out, err):

            # Given
            self.scheduler.config_file = None

            # When
            self.scheduler.run()

            # Then
            # Check the output.
            self.assertEqual(len(self.scheduler.mowers), 0)

    def test__given_invalid_config_file__when_run__then_nothing_happens(self):

        with captured_output() as (out, err):

            # Given
            self.scheduler.config_file = "This should be a loaded instance of lawnmower.src.config_file.ConfigFile"

            # When
            self.scheduler.run()

            # Then
            # Check the output.
            self.assertEqual(len(self.scheduler.mowers), 0)

    def test__given_not_initialized_config_file__when_run__then_nothing_happens(self):

        with captured_output() as (out, err):

            # Given
            config_file_mock = Mock()
            config_file_mock.lawn_x_max = None
            config_file_mock.lawn_y_max = None
            config_file_mock.mowers = None
            self.scheduler.config_file = config_file_mock

            # When
            self.scheduler.run()

            # Then
            # Check the output.
            self.assertEqual(len(self.scheduler.mowers), 0)

    def test__given_valid_empty_config_file__when_run__then_ok(self):

        with captured_output() as (out, err):

            # Given
            config_file_mock = Mock()
            config_file_mock.lawn_x_max = "3"
            config_file_mock.lawn_y_max = "4"
            config_file_mock.mowers = []
            self.scheduler.config_file = config_file_mock

            # When
            self.scheduler.run()

            # Then
            # Check the output.
            self.assertEqual(len(self.scheduler.mowers), 0)

    def test__given_valid_config_file_and_no_mower_overlapping__when_run__then_ok(self):

        with captured_output() as (out, err):

            # Given
            config_file_mock = Mock()
            config_file_mock.lawn_x_max = "5"
            config_file_mock.lawn_y_max = "5"

            mower1_info = {"initial_orientation": "N", "initial_position": (1, 2), "instruction_list": "LFLFLFLFF"}
            # Notice that mower2 starts just facing the expected final position of mower1
            mower2_info = {"initial_orientation": "S", "initial_position": (1, 4), "instruction_list": "FFRFFRFRRF"}

            config_file_mock.mowers = [mower1_info, mower2_info]
            self.scheduler.config_file = config_file_mock
            self.scheduler.mower_overlapping = False

            # When
            self.scheduler.run()

            # Then
            self.assertEqual(len(self.scheduler.mowers), 2)

            self.assertEqual(self.scheduler.mowers[0].x, 1)
            self.assertEqual(self.scheduler.mowers[0].y, 3)
            self.assertEqual(self.scheduler.mowers[0].orientation.get_str(), "N")

            self.assertEqual(self.scheduler.mowers[1].x, 0)
            self.assertEqual(self.scheduler.mowers[1].y, 4)
            self.assertEqual(self.scheduler.mowers[1].orientation.get_str(), "S")

    def test__given_valid_config_file_and_mower_overlapping__when_run__then_ok(self):

        with captured_output() as (out, err):

            # Given
            config_file_mock = Mock()
            config_file_mock.lawn_x_max = "5"
            config_file_mock.lawn_y_max = "5"

            mower1_info = {"initial_orientation": "N", "initial_position": (1, 2), "instruction_list": "LFLFLFLFF"}
            # Notice that mower2 starts just facing the expected final position of mower1
            mower2_info = {"initial_orientation": "S", "initial_position": (1, 4), "instruction_list": "FRFRFRRF"}

            config_file_mock.mowers = [mower1_info, mower2_info]
            self.scheduler.config_file = config_file_mock
            self.scheduler.mower_overlapping = True

            # When
            self.scheduler.run()

            # Then
            self.assertEqual(len(self.scheduler.mowers), 2)

            self.assertEqual(self.scheduler.mowers[0].x, 1)
            self.assertEqual(self.scheduler.mowers[0].y, 3)
            self.assertEqual(self.scheduler.mowers[0].orientation.get_str(), "N")

            self.assertEqual(self.scheduler.mowers[1].x, 0)
            self.assertEqual(self.scheduler.mowers[1].y, 3)
            self.assertEqual(self.scheduler.mowers[1].orientation.get_str(), "S")

    @patch("lawnmower.src.scheduler.Scheduler.print")
    def test__given_valid_config_file_and_no_verbose__when_run__then_ok(self, print_mock):

        with captured_output() as (out, err):

            # Given
            config_file_mock = Mock()
            config_file_mock.lawn_x_max = "5"
            config_file_mock.lawn_y_max = "5"

            mower1_info = {"initial_orientation": "N", "initial_position": (1, 2), "instruction_list": "LFLFLFLFF"}
            mower2_info = {"initial_orientation": "E", "initial_position": (3, 3), "instruction_list": "FFRFFRFRRF"}

            config_file_mock.mowers = [mower1_info, mower2_info]
            self.scheduler.config_file = config_file_mock

            # When
            self.scheduler.run()

            # Then
            self.assertEqual(len(self.scheduler.mowers), 2)

            self.assertEqual(self.scheduler.mowers[0].x, 1)
            self.assertEqual(self.scheduler.mowers[0].y, 3)
            self.assertEqual(self.scheduler.mowers[0].orientation.get_str(), "N")

            self.assertEqual(self.scheduler.mowers[1].x, 5)
            self.assertEqual(self.scheduler.mowers[1].y, 1)
            self.assertEqual(self.scheduler.mowers[1].orientation.get_str(), "E")

            print_mock.assert_not_called()

    @patch("lawnmower.src.scheduler.Scheduler.print")
    def test__given_valid_config_file_and_verbose__when_run__then_ok(self, print_mock):

        with captured_output() as (out, err):

            # Given
            config_file_mock = Mock()
            config_file_mock.lawn_x_max = "5"
            config_file_mock.lawn_y_max = "5"

            mower1_info = {"initial_orientation": "N", "initial_position": (1, 2), "instruction_list": "LFLFLFLFF"}
            mower2_info = {"initial_orientation": "E", "initial_position": (3, 3), "instruction_list": "FFRFFRFRRF"}

            config_file_mock.mowers = [mower1_info, mower2_info]
            self.scheduler.config_file = config_file_mock

            # When
            self.scheduler.run(verbose=True)

            # Then
            self.assertEqual(len(self.scheduler.mowers), 2)

            self.assertEqual(self.scheduler.mowers[0].x, 1)
            self.assertEqual(self.scheduler.mowers[0].y, 3)
            self.assertEqual(self.scheduler.mowers[0].orientation.get_str(), "N")

            self.assertEqual(self.scheduler.mowers[1].x, 5)
            self.assertEqual(self.scheduler.mowers[1].y, 1)
            self.assertEqual(self.scheduler.mowers[1].orientation.get_str(), "E")

            print_mock.assert_called()
