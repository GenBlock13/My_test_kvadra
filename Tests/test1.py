import pytest
from Equation import solve_linear
def test():
    def test_linear():
        assert solve_linear(-7, 7) == 'Equation root is 1.0'


    def test_linear_zero1():
        assert solve_linear(0, 7) == 'No solution'


    def test_linear_zero2():
        assert solve_linear(0, 0) == 'Any X solves equation'


if __name__ == '__main__':
    pytest(test)
