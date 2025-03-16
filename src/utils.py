from src.constants import OutputString


class FizzbuzzCalculator:
    """Calculator class for fizzbuzz. Designed
    to determine whether an integer is fizz, buzz
    or fizzbuzz, and pass back the correct string.
    """

    def __init__(self, value: int, *args, **kwargs):
        self.value = value

    @property
    def is_fizz(self) -> bool:
        if self.value % 3 == 0:
            return True
        return False

    @property
    def is_buzz(self) -> bool:
        if self.value % 5 == 0:
            return True
        return False

    def get_fizzbuzz_value(self) -> str:
        """Returns the correct fizzbuzz string
        based on the numerical value passed.
        """
        output = ""

        if self.is_fizz:
            output += OutputString.FIZZ

        if self.is_buzz:
            output += OutputString.BUZZ

        return output

    def get_output_string(self) -> str:
        """Return full output string for stdout, including
        the value initially passed."""
        fizzbuzz_value = self.get_fizzbuzz_value()
        return f"{self.value} {fizzbuzz_value}"
