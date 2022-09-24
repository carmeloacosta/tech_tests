import sys
from os.path import abspath, dirname


def add_root_path():
    """
        Adds the project's root path to the environment's path, in order to allow
        importing project's modules.

    :return: None
    """
    # To allow importing LawnMower's stuff using lawnmower.*
    project_dir_path = abspath(dirname(dirname(dirname(__file__))))

    if project_dir_path not in sys.path:
        sys.path.insert(0, project_dir_path)


add_root_path()
