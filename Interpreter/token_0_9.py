from Interpreter.interface import *
from Interpreter.token import *

DIGITS_0_9 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


class Tokenizer0_9(TokenizerInterface):
    def __init__(self):
        super().__init__()

    def interpret(self, string, position):
        if  not self._check_bounds(string, position):
            return ERROR
        if string[position] in DIGITS_0_9:
            return Token(TOKEN_NUMBER, string[position], 1)
        else:
            return Token(TOKEN_EMPTY, '', 0)
