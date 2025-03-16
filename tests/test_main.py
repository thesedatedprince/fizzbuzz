import pytest

from src.constants import ErrorMessage
from src.main import fizzbuzz

# 1. Take two integers between 1 and 100
# Function must validate type of both arguments
# Function much validate each argument is between 1 and 100


@pytest.mark.parametrize(
    "start,end,error_message",
    [
        (
            "test",
            1,
            ErrorMessage.INCORRECT_INPUT_TYPE.format(index=0, input_type="str"),
        ),
        (
            100,
            "test",
            ErrorMessage.INCORRECT_INPUT_TYPE.format(index=1, input_type="str"),
        ),
        (
            "test",
            "test1",
            "\n".join(
                [
                    ErrorMessage.INCORRECT_INPUT_TYPE.format(index=0, input_type="str"),
                    ErrorMessage.INCORRECT_INPUT_TYPE.format(index=1, input_type="str"),
                ]
            ),
        ),
    ],
)
def test_fizzbuzz_input_validates_type(start, end, error_message):
    with pytest.raises(TypeError) as e:
        fizzbuzz(start, end)
    assert error_message in str(e.value)


@pytest.mark.parametrize(
    "start,end,error_message",
    [
        (0, 40, ErrorMessage.INCORRECT_INPUT_VALUE.format(index=0, value=0)),
        (40, 0, ErrorMessage.INCORRECT_INPUT_VALUE.format(index=1, value=0)),
        (101, 40, ErrorMessage.INCORRECT_INPUT_VALUE.format(index=0, value=101)),
        (40, 101, ErrorMessage.INCORRECT_INPUT_VALUE.format(index=1, value=101)),
        (
            0,
            101,
            "\n".join(
                [
                    ErrorMessage.INCORRECT_INPUT_VALUE.format(index=0, value=0),
                    ErrorMessage.INCORRECT_INPUT_VALUE.format(index=1, value=101),
                ]
            ),
        ),
    ],
)
def test_fizzbuzz_input_validates_value_boundary(start, end, error_message):
    with pytest.raises(ValueError) as e:
        fizzbuzz(start, end)
    assert error_message in str(e.value)


def test_fizzbuzz_prints_value_of_each_argument(capsys):
    fizzbuzz(1, 10)

    captured = capsys.readouterr()

    for i in range(1, 10):
        assert str(i) in captured.out


def test_fizzbuzz_prints_fizz_if_only_divisible_by_3(capsys):
    fizzbuzz(1, 100)

    captured = capsys.readouterr()

    captured_lines = captured.out.split("\n")[:-1]

    for line in captured_lines:
        line_num_to_value = line.split(" ")

        # For the purposes of this test, ignore values
        # that could potentially output "fizzbuzz"
        if int(line_num_to_value[0]) % 5 == 0:
            continue

        if int(line_num_to_value[0]) % 3 == 0:
            assert line_num_to_value[1] == "fizz"


def test_fizzbuzz_prints_buzz_if_only_divisible_by_5(capsys):
    fizzbuzz(1, 100)

    captured = capsys.readouterr()

    captured_lines = captured.out.split("\n")[:-1]

    for line in captured_lines:
        line_num_to_value = line.split(" ")

        # For the purposes of this test, ignore values
        # that could potentially output "fizzbuzz"
        if int(line_num_to_value[0]) % 3 == 0:
            continue

        if int(line_num_to_value[0]) % 5 == 0:
            assert line_num_to_value[1] == "buzz"


def test_fizzbuzz_prints_fizzbuzz_if_divisible_by_3_and_5(capsys):
    fizzbuzz(1, 100)

    captured = capsys.readouterr()

    captured_lines = captured.out.split("\n")[:-1]

    for line in captured_lines:
        line_num_to_value = line.split(" ")

        if int(line_num_to_value[0]) % 5 == 0 and int(line_num_to_value[0]) % 3 == 0:
            assert line_num_to_value[1] == "fizzbuzz"
