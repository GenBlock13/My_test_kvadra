from turtle import position

from Interpreter.token_0_9 import *
from Interpreter.token import *
from Interpreter.interface import *


class Tokenizer0_9s(TokenizerInterface):
    def __init__(self):
        super().__init__()
        self.tokenizer = Tokenizer0_9s

    def interpret(self, string, position):
        if not self._check_bounds(string, position):
            return EMPTY
       result = ''
       token = self.tokenizer(interpret(string, position))
