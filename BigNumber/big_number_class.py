from string import digits


class BigNumber:

    def __init__(self, integer_part, fractional_part, exponent):
        self.integer_part = integer_part
        self.fractional_part = fractional_part
        self.exponent = exponent

    def __str__(self):
        return f"{self.integer_part}.{self.fractional_part}e{self.exponent}"

    def input(self):



    def __add__(self, other):

