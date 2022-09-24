import io
import os
import sys
import logging
import contextlib
from subprocess import Popen, PIPE

stdout = None
stderr = None


def Any(cls):
    """
        To be used in assert matching with (e.g., assert_called_with) when an argument type is not important.

    :param cls: (class) Basic class (e.g., int, MyClass)
    :return: (function)
    """
    class Any(cls):
        def __eq__(self, other):
            return True

    return Any()


def get_fixtures_path():
    """
        Returns the path to the project's fixtures folder, to be used in the tests.

    :return: None
    """
    return os.path.join(os.path.dirname(__file__), "fixtures")


def os_system_mock(arg):
    """
        Mocks OS system.

    :param arg: (str) Command to mock
    :return: None
    """
    global stdout, stderr
    p = Popen(arg, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()


@contextlib.contextmanager
def captured_output(capture=True, mock_os_system=True):
    """
        Allows to capture system output to stdout/stderr, thus yielding nicer tests.
        To be used in a context manager, within a test, to capture output.

        Example:

        ...
        with captured_output() as (out, err):
            try:
                parser.parse_args(args)
                return True

            except SystemExit as e:
                return False
        ...

    :return: None
    """
    global stdout, stderr

    if not capture:
        logging.disable(logging.NOTSET)
        yield None, None

    else:
        logging.disable()
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        if mock_os_system:
            saved_os_system = os.system
            os.system = os_system_mock
        try:
            sys.stdout, sys.stderr = new_out, new_err
            if stdout is not None:
                new_out.write(stdout)
            if stderr is not None:
                new_err.write(stderr)
            yield sys.stdout, sys.stderr

        finally:
            sys.stdout, sys.stderr = old_out, old_err
            if mock_os_system:
                os.system = saved_os_system
            stdout, stderr = (None, None)
