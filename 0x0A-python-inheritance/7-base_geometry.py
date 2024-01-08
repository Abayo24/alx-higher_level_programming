 #!/usr/bin/python3
"""BaseGeometry with Public instance method"""


class BaseGeometry:
    """BaseGeometry with Public instance method"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:

            raise ValueError(f"{name} must be greater than 0")

