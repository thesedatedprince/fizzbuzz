from src.validators import InputValidator


def fizzbuzz(start: int, end: int):
    InputValidator(start, end).validate()

    for i in range(start, end):
        val = f"{i}"
        if i % 3 == 0:
            val += " fizz"
        print(val)
