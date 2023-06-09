from Interpreter.interface import *
from Interpreter.token import *



class Tokenizer_dot(TokenizerInterface):
    def __init__(self):
        super().__init__()

    def interpret(self, string, position):
        if  not self._check_bounds(string, position):
            return ERROR

        if (string[position] == '.'):
            return Token(TOKEN_DOT, string[position], 1)
        else:
            return Token(TOKEN_EMPTY, '', 0)
