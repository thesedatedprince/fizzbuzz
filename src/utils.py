from src.constants import OutputString


class FizzbuzzCalculator:

    def __init__(self, value, *args, **kwargs):
        self.value = value

    @property
    def is_fizz(self):
        if self.value % 3 == 0:
            return True
        return False

    @property
    def is_buzz(self):
        if self.value % 5 == 0:
            return True
        return False

    def get_fizzbuzz_value(self):
        output = ""

        if self.is_fizz:
            output += OutputString.FIZZ

        if self.is_buzz:
            output += OutputString.BUZZ

        return output

    def get_output_string(self):
        fizzbuzz_value = self.get_fizzbuzz_value()
        return f"{self.value} {fizzbuzz_value}"
