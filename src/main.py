from src.validators import InputValidator


def fizzbuzz(start: int, end: int):
    InputValidator(start, end).validate()

    for i in range(start, end):
        print(i)
