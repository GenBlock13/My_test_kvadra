from abc import ABC
from Interpreter.token import *


ERROR = Token(TOKEN_EMPTY, '', 0)


class TokenizerInterface:
    def __init__(self):
        pass

    def _check_bounds(self, string, position):
        l = len(string)
        if position < 0 or position >= l:
            return False
        return True



    def interpret(self, string, position):
        pass
