from typing import Tuple, Union

from src.constants import ErrorMessage


class InputValidator:
    def __init__(self, start: Union[int, str], end: Union[int, str], *args, **kwargs):
        self.start = start
        self.end = end

    def is_valid_input_type(self, value: Union[int, str]) -> bool:
        """Determines validity of input type.

        Input is valid if an int, or digit as string - i.e '3' - is passed.
        """
        if type(value) is not int and not value.isdigit():  # type: ignore
            return False
        return True

    def is_valid_input_value(self, value: Union[int, str]) -> bool:
        """Determines validity of input value.

        Input is valid if between 1 and 100."""
        value = int(value)
        if value < 1 or value > 100:
            return False
        return True

    def join_error_output(self, error_messages: list) -> str:
        """Join multiple error messages into single string in case
        of multiple arguments failing validation."""
        return "\n".join(error_messages)

    def validate(self):
        type_validation_errors = []
        value_validation_errors = []

        # Note: this implementation is to save a cycle of needing
        # to iterate over the same list twice, once for type and once
        # for value validation.
        for index, value in enumerate([self.start, self.end]):
            if not self.is_valid_input_type(value):
                type_validation_errors.append(
                    ErrorMessage.INCORRECT_INPUT_TYPE.format(
                        index=index, input_type=type(value).__name__
                    )
                )
            # If we have any type validation errors don't bother
            # validating for value - it isn't an integer or digit,
            # so it's going to fail the test on whether it's between
            # 1 and 100.
            if len(type_validation_errors) > 0:
                continue

            if not (self.is_valid_input_value(value)):
                value_validation_errors.append(
                    ErrorMessage.INCORRECT_INPUT_VALUE.format(index=index, value=value)
                )

        if len(type_validation_errors) > 0:
            raise TypeError(self.join_error_output(type_validation_errors))

        if len(value_validation_errors) > 0:
            raise ValueError(self.join_error_output(value_validation_errors))

    def get_validated_values(self) -> Tuple[int, int]:
        """Run validation, and return values as integers if valid."""
        self.validate()
        return int(self.start), int(self.end)
