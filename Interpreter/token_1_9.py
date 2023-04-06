from Interpreter.interface import *
from Interpreter.token import *

DIGITS_1_9 = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


class Tokenizer1_9(TokenizerInterface):
    def __init__(self):
        super().__init__()

    def interpret(self, string, position):
        if  not self._check_bounds(string, position):
            return EMPTY


        if string[position] in DIGITS_1_9:
            return Token(TOKEN_INTEGER, string[position], 1)
        else:
            return Token(TOKEN_EMPTY, '', 0)
