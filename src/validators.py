from src.constants import ErrorMessage


class InputValidator:
    def __init__(self, start, end, *args, **kwargs):
        self.start = start
        self.end = end

    def is_valid_input_type(self, value):
        if type(value) is not int and not value.isdigit():
            return False
        return True

    def is_valid_input_value(self, value):
        value = int(value)
        if value < 1 or value > 100:
            return False
        return True

    def join_error_output(self, error_messages):
        return "\n".join(error_messages)

    def validate(self):
        type_validation_errors = []
        value_validation_errors = []
        for index, value in enumerate([self.start, self.end]):
            if not self.is_valid_input_type(value):
                type_validation_errors.append(
                    ErrorMessage.INCORRECT_INPUT_TYPE.format(
                        index=index, input_type=type(value).__name__
                    )
                )
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

    def get_validated_values(self):
        self.validate()
        return int(self.start), int(self.end)
