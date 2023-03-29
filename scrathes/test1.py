import pytest


def solve_linear(b, c):
    if b != 0:
        x = - c / b
        return x
    else:
        if c == 0:
            return 'Any X solves equation'
        else:
            return 'No solution'


print(solve_linear(5, 5))
