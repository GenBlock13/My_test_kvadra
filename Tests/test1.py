import pytest

from Equation.solving_linear import solve_linear
from Interpreter.token_0_9 import *
from Interpreter.token_1_9 import *

def test_linear():
    assert solve_linear(-7, 7) == 'Equation root is 1.0'


def test_linear_zero1():
    assert solve_linear(0, 7) == 'No solution'


def test_linear_zero2():
    assert solve_linear(0, 0) == 'Any X solves equation'


numb_test = '0123456789'
t1 = Tokenizer0_9()
t2 = Tokenizer1_9()
def test_interpret():
    assert str(t1.interpret(numb_test, 1)) == 'integer: 1'

def test_interpret():
    assert str(t1.interpret(numb_test, 3)) == 'integer: 3'

def test_interpret():
    assert str(t1.interpret(numb_test, 0)) == 'integer: 0'

def test_interpret1():
    assert str(t2.interpret(numb_test, 0)) == 'empty: '

def test_interpret1():
    assert str(t2.interpret(numb_test, 1)) == 'integer: 1'