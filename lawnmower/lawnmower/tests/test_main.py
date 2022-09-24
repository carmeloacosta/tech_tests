import sys
from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock

import lawnmower.src.config_file
from lawnmower.src.main import main
from lawnmower.tests.testutils import captured_output, Any


class TestMain(TestCase):

    def setUp(self):
        # Save a copy of command line arguments to mock them during tests
        self.sys_argv = deepcopy(sys.argv)

    def tearDown(self):
        # Restore command line arguments
        sys.argv = self.sys_argv

    @patch("lawnmower.src.scheduler.Scheduler", autospec=True)
    @patch("lawnmower.src.config_file.ConfigFile", autospec=True)
    def test__given_no_command_line_arguments__when_main__then_nothing_happens(self, config_file_mock, scheduler_mock):

        with captured_output() as (out, err):

            # Given
            # Mock command line arguments
            sys.argv = sys.argv[:1]     # RECALL that the first position always the name of the program

            # When
            main()

            # Then
            config_file_mock.assert_not_called()
            scheduler_mock.assert_not_called()

    @patch("lawnmower.src.scheduler.Scheduler", autospec=True)
    @patch("lawnmower.src.config_file.ConfigFile.load")
    def test__given_one_command_line_arguments_and_not_successful_load__when_main__then_nothing_happens(
            self, config_file_load_mock, scheduler_mock):

        with captured_output() as (out, err):

            # Given
            # Mock command line arguments
            sys.argv = sys.argv[:1]     # RECALL that the first position always the name of the program

            input_filepath = "path/to/whatever_config_file.txt"
            sys.argv.append(input_filepath)

            # Mock not successful load
            config_file_load_mock.return_value = False

            # When
            main()

            # Then
            config_file_load_mock.assert_called_once_with(input_filepath)
            scheduler_mock.assert_not_called()

    @patch("lawnmower.src.scheduler.Scheduler", autospec=True)
    @patch("lawnmower.src.config_file.ConfigFile.load")
    def test__given_one_command_line_arguments_and_successful_load__when_main__then_ok(
            self, config_file_load_mock, scheduler_mock):

        with captured_output() as (out, err):

            # Given
            # Mock command line arguments
            sys.argv = sys.argv[:1]     # RECALL that the first position always the name of the program

            input_filepath = "path/to/whatever_config_file.txt"
            sys.argv.append(input_filepath)

            # Mock successful load
            config_file_load_mock.return_value = True

            # Mock Scheduler
            mocked_scheduler = Mock()
            scheduler_mock.return_value = mocked_scheduler

            # When
            main()

            # Then
            config_file_load_mock.assert_called_once_with(input_filepath)
            scheduler_mock.assert_called_once_with(config_file=Any(lawnmower.src.config_file.ConfigFile),
                                                   mower_overlapping=False)
            mocked_scheduler.run.assert_called_once_with(verbose=False)

    @patch("lawnmower.src.scheduler.Scheduler", autospec=True)
    @patch("lawnmower.src.config_file.ConfigFile.load")
    def test__given_two_command_line_arguments_and_successful_load_and_verbose__when_main__then_ok(
            self, config_file_load_mock, scheduler_mock):

        with captured_output() as (out, err):

            # Given
            # Mock command line arguments
            sys.argv = sys.argv[:1]     # RECALL that the first position always the name of the program

            input_filepath = "path/to/whatever_config_file.txt"
            verbose = "T"
            sys.argv.append(input_filepath)
            sys.argv.append(verbose)

            # Mock successful load
            config_file_load_mock.return_value = True

            # Mock Scheduler
            mocked_scheduler = Mock()
            scheduler_mock.return_value = mocked_scheduler

            # When
            main()

            # Then
            config_file_load_mock.assert_called_once_with(input_filepath)
            scheduler_mock.assert_called_once_with(config_file=Any(lawnmower.src.config_file.ConfigFile),
                                                   mower_overlapping=False)
            mocked_scheduler.run.assert_called_once_with(verbose=True)

    @patch("lawnmower.src.scheduler.Scheduler", autospec=True)
    @patch("lawnmower.src.config_file.ConfigFile.load")
    def test__given_three_command_line_arguments_and_successful_load_and_verbose_and_overlapping__when_main__then_ok(
            self, config_file_load_mock, scheduler_mock):

        with captured_output() as (out, err):

            # Given
            # Mock command line arguments
            sys.argv = sys.argv[:1]     # RECALL that the first position always the name of the program

            input_filepath = "path/to/whatever_config_file.txt"
            verbose = "T"
            mower_overlapping = "T"

            sys.argv.append(input_filepath)
            sys.argv.append(verbose)
            sys.argv.append(mower_overlapping)

            # Mock successful load
            config_file_load_mock.return_value = True

            # Mock Scheduler
            mocked_scheduler = Mock()
            scheduler_mock.return_value = mocked_scheduler

            # When
            main()

            # Then
            config_file_load_mock.assert_called_once_with(input_filepath)
            scheduler_mock.assert_called_once_with(config_file=Any(lawnmower.src.config_file.ConfigFile),
                                                   mower_overlapping=True)
            mocked_scheduler.run.assert_called_once_with(verbose=True)
