import sys
from typing import Union

from src.utils import FizzbuzzCalculator
from src.validators import InputValidator


def run(start: Union[int, str], end: Union[int, str]):
    validated_start, validated_end = InputValidator(start, end).get_validated_values()

    for index in range(validated_start, validated_end + 1):
        fizzbuzz_generator = FizzbuzzCalculator(index)
        print(fizzbuzz_generator.get_output_string())


if __name__ == "__main__":
    command_line_args = sys.argv

    if len(command_line_args) != 3:
        raise RuntimeError("A start value and end value must be passed.")

    start = command_line_args[1]
    end = command_line_args[2]

    run(start, end)
