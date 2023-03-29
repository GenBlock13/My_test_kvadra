import pytest


def solve_linear(b, c):
    if b != 0:
        x = - c / b
        return 'Equation root is {0:.5}'.format(x)
    else:
        if c == 0:
            return 'Any X solves equation'
        else:
            return 'No solution'


def test_linear():
    assert solve_linear(-7, 7) == 'Equation root is 1.0'

def test_linear_zero1():
    assert solve_linear(0, 7) == 'No solution'

def test_linear_zero2():
    assert solve_linear(0, 0) == 'Any X solves equation'


if __name__ == '__main__':
    pytest(main)

