import re

from util.util import ValidationRegex


class Validator:
    def email_validator(self, value):
        if not re.match(ValidationRegex.EMAIL.value, value):
            raise ValueError("Invalid email format")

        return value