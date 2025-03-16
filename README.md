# Fizzbuzz

This demonstrates a Fizzbuzz implementation. It is designed to be defensively coded,
with strict validation on inputs.


## Setup

Note: Please ensure python3.11.11 is installed and available on your machine.

This project uses `pipenv` to manage dependencies. Installation instructions can be
found [here](https://pipenv.pypa.io/en/latest/installation.html#installing-packages-for-your-project).

Once `pipenv` is installed, run the following to activate the shell:

    pipenv shell

And then install dependencies:

    pipenv install --dev

Finally, this project uses `pre-commit` to enforce code standards. Use the following
commend to install the commit hooks:

    pre-commit install


## Running Tests

This project uses `pytest`, with the `pytest-xdist` package installed to allow
for parallel running. Run the tests with the following command:

    pytest tests/ -n auto


## Running the Code

The script is designed to be run from the command line. Run the script with the following
command:

    python -m src.main <arg1> <arg2>

## Code Style Notes

I've gone for readability over implementations that are more terse. Hence, I've
aimed for more verbose behaviour, rather than "trick" solutions like:

    "Fizz"*(not n % 3) + "Buzz"*(not n % 5) or n

Which are leaner, but less readable.

## Notes for further iterations

All the tests are currently going via the `run` function, as I was coding to that
then refactoring. Many of the tests could also be refactored to point at the
specific classes/functions rather than running the whole script end-to-end each
time.
