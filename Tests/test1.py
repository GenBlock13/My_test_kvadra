import pytest

from Equation.solving_linear import solve_linear
from Interpreter.interpret_0_9 import *
from Interpreter.interpret_1_9 import *

def test_linear():
    assert solve_linear(-7, 7) == 'Equation root is 1.0'


def test_linear_zero1():
    assert solve_linear(0, 7) == 'No solution'


def test_linear_zero2():
    assert solve_linear(0, 0) == 'Any X solves equation'



# def test_interpret():
#     assert t1.interpret(test_set, 1) == TOKEN_INTEGER.

