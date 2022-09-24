# TECHNICAL TEST : LAWNMOWER

Automatic lawn mower designed to mow rectangular surfaces.

# Use

Next sections describe how to run the lawnmower software. 

## Command line

To directly run from Linux (developed in Ubuntu 22.04 with Python 3.9), and assuming you are already in the same folder
as this readme file, all you have to do is executing the following command from a terminal:

    PYTHONPATH=<lawnmower/path> python3 src/main.py <path/to/config_file>    

with:

  <lawnmower/path> = Absolute path to lawnmower folder (e.g., /home/carmelo/tech_tests/lawnmower)
  <config_file>        = Path to the text file including lawnmower configuration (e.g., conf/input.txt)
  
Example:

    PYTHONPATH=/home/carmelo/tech_tests/lawnmower python3 src/main.py conf/input.txt

Notice that you need to have installed Python 3.9+ to be able to run this command.

## Docker

You can also run it from docker. Assuming you are already in the same folder as this readme file, all you have to do is 
executing the following commands from a terminal: 

    docker build -t lawnmower .
    docker run lawnmower

Notice that you need to have installed docker (tested 20.10.12) to be able to run this command.

# Development

Next sections describe how to run lawnmower software unit tests, so that you could be able to properly maintain it. 

## Command line

To directly run the unit tests from Linux (developed in Ubuntu 22.04 with Python 3.9), and assuming you are already in 
the same folder as this readme file, all you have to do is executing the following commands from a terminal:

    pip install -r test_requirements.txt
    python -m pytest --cov=src/ --cov-branch -vvv --cov-report term-missing --color=yes -s tests

Notice that the first line install the testing requirements. If you have them already installed you can simply skip that 
first line. The second line runs all tests, showing the code coverage.

In order to run a single test simply execute the following command:

    python -m pytest -vvv -s <path>/<to>/<test_file>::<TestCaseName>::<test_name>

Example:

    python -m pytest -vvv -s tests/test_config_file.py::TestConfigFile::test__given_incomplete_first_line__when_load__then_return_false

## Docker

You can also run the unit tests from docker, without needing to install any dependency in your machine. Assuming you 
have already built the docker image, as described above, and you are already in the same folder as this readme file,
all you have to do is executing the following command from a terminal: 

    docker run  --mount src=$( pwd)/,dst=/lawnmower,type=bind -it --entrypoint bash lawnmower

This command will start an interactive session in the lawnmower, mounting the lawnmower folder in your local machine on
the image. This way you can run the unit tests, either all of them or a single one (as specified above), from within
the running docker image, without needing to install any dependency in your machine, but keeping all modifications to 
your code.
