import enum


class ErrorMessage(enum.StrEnum):
    INCORRECT_INPUT_TYPE = (
        "Expected type integer for argument {index}, received type {input_type}."
    )
    INCORRECT_INPUT_VALUE = (
        "Expected value between 1 and 100 for argument {index}, received {value}."
    )


class OutputString(enum.StrEnum):
    FIZZ = "fizz"
    BUZZ = "buzz"
