from Interpreter.token_sign import *
from Interpreter.token_n import *

from Interpreter.token import *
from Interpreter.interface import *


class Tokenizer_Z(TokenizerInterface):
    def __init__(self):
        super().__init__()
        self.tokenizer_n = Tokenizer_N()
        self.tokenizer_sign = Tokenizer_sign()

    def interpret(self, string, position):
        if not self._check_bounds(string, position):
            return EMPTY
        current = position

        token_sign = self.tokenizer_sign.interpret(string, position)
        if token_sign.type != TOKEN_EMPTY:
            position += token_sign.lenght

        token_n = self.tokenizer_n.interpret(string, position)

        if token_n.type != TOKEN_EMPTY:
            return Token(TOKEN_INTEGER, token_sign.value + token_n.value, token_sign.lenght + token_n.lenght)
        else:
            return EMPTY
