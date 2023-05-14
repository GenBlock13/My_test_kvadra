from Interpreter.token_0_9_plus import *
from Interpreter.token_1_9 import *
from Interpreter.token_0_9 import *
from Interpreter.token import *
from Interpreter.interface import *


class Tokenizer_N(TokenizerInterface):
    def __init__(self):
        super().__init__()
        self.tokenizer_0_9_plus = Tokenizer0_9_plus()
        self.tokenizer_1_9 = Tokenizer1_9()
        self.tokenizer_0_9 = Tokenizer0_9()

    def interpret(self, string, position):
        if not self._check_bounds(string, position):
            return ERROR
        current = position

        token_1_9 = self.tokenizer_1_9.interpret(string, position)
        if token_1_9.type != TOKEN_EMPTY:
            token_0_9_plus = self.tokenizer_0_9_plus.interpret(string, position + token_1_9.lenght)

            if token_0_9_plus.type != TOKEN_EMPTY:
                return Token(TOKEN_NUMBER, token_1_9.integer + token_0_9_plus.integer,
                             token_1_9.lenght + token_0_9_plus.lenght)
            else:
                return token_1_9
        else:
            token_0_9 = self.tokenizer_0_9.interpret(string, position)

            if token_0_9.type != TOKEN_EMPTY:
                return token_0_9
            else:
                return ERROR
