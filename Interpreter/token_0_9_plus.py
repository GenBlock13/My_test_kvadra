from turtle import position

from Interpreter.token_0_9 import *
from Interpreter.token import *
from Interpreter.interface import *


class Tokenizer0_9_plus(TokenizerInterface):
    def __init__(self):
        super().__init__()
        self.tokenizer = Tokenizer0_9()

    def interpret(self, string, position):
        if not self._check_bounds(string, position):
            return ERROR
        current = position

        token = self.tokenizer.interpret(string, position)
        while token.type != TOKEN_EMPTY:
            if not self._check_bounds(string, current + token.lenght):
                current += token.lenght
                token = self.tokenizer.interpret(string, current)
            else:
                return Token(TOKEN_NUMBER, string[position:], len(string) - position)



        return Token(TOKEN_NUMBER, string[position: current], current - position)
