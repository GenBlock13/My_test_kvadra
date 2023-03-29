from math import sqrt
from cmath import sqrt


class QuadraticInput():
    def __init__(self, str, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.str = str


class InputString():
    def __init__(self, str):
        self.str = str

    def check_input_string(self):
        if len(self.str) != 3:
            return False
        else:
            return True

    @property
    def get_float(self):
        if self.str not isnumeric:
            return False
        else:
            a = float(self.str[0])
            b = float(self.str[1])
            c = float(self.str[2])


my_input = input().split(' ')

equation = InputString(my_input)

print(equation)