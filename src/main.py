import enum


class ErrorMessage(enum.StrEnum):
    INCORRECT_INPUT_TYPE = (
        "Expected type integer for argument {index}, received type {input_type}."
    )


def validate_input_type(start: int, end: int):
    input_validation_errors = []
    for index, value in enumerate([start, end]):
        if type(value) is not int:
            input_validation_errors.append(
                ErrorMessage.INCORRECT_INPUT_TYPE.format(
                    index=index, input_type=type(value).__name__
                )
            )
    if len(input_validation_errors) > 0:
        raise TypeError("\n".join(input_validation_errors))


def fizzbuzz(start: int, end: int):
    validate_input_type(start, end)
