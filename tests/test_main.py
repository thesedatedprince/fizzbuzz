import pytest

from src.main import ErrorMessage, fizzbuzz

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
