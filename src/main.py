import sys
from typing import Union

from src.utils import FizzbuzzCalculator
from src.validators import InputValidator


def run(start: Union[int, str], end: Union[int, str]):
    """Run the fizzbuzz function, including validation.

    Note, while this does accept a Union of int or string,
    if a string is passed, it must be a digit to allow the
    validator to return an integer. This is to handle
    string input from the command line.
    """
    validated_start, validated_end = InputValidator(start, end).get_validated_values()

    # NOTE: Spec didn't specify if the start number is lower than the end number
    # so we handle that case here
    iteration_range = range(validated_start, validated_end + 1)
    if validated_start > validated_end:
        iteration_range = range(validated_start, validated_end - 1, -1)

    # NOTE: Spec was taken to mean end value inclusive, hence the + 1
    for index in iteration_range:
        fizzbuzz_generator = FizzbuzzCalculator(index)
        print(fizzbuzz_generator.get_output_string())


if __name__ == "__main__":
    command_line_args = sys.argv

    if len(command_line_args) != 3:
        raise RuntimeError("A start value and end value must be passed.")

    start = command_line_args[1]
    end = command_line_args[2]

    run(start, end)
