from Interpreter.token_1_9 import *
from Interpreter.token_sign import *
from Interpreter.token_q import *
from Interpreter.token_exp import *
from Interpreter.token_0_9_plus import *
from Interpreter.token import *


class Tokenizer_R(TokenizerInterface):
    def __init__(self):
        super().__init__()
        self.tokenizer_q = Tokenizer_Q()
        self.tokenizer_exp = Tokenizer_exp()
        self.tokenizer_0_9_plus = Tokenizer0_9_plus()
        self.tokenizer_sign = Tokenizer_sign()
        self.tokenizer_1_9 = Tokenizer1_9()

    def interpret(self, string, position):
        if not self._check_bounds(string, position):
            return ERROR

        current = position
        token_q = self.tokenizer_q.interpret(string, current)
        if token_q.type != TOKEN_EMPTY:
            current += token_q.lenght
            token_exp = self.tokenizer_exp.interpret(string, current)

            if token_exp.type != TOKEN_EMPTY:
                current += token_exp.lenght
                token_sign = self.tokenizer_sign.interpret(string, current)

                if token_sign.type != TOKEN_EMPTY:
                    current += token_sign.lenght
                token_1_9 = self.tokenizer_1_9.interpret(string, current)

                if token_1_9.type != TOKEN_EMPTY:
                    current += token_1_9.lenght
                    token_0_9_plus = self.tokenizer_0_9_plus.interpret(string, current)

                    if token_0_9_plus.type != TOKEN_EMPTY:
                        return Token(TOKEN_NUMBER,
                                     token_q.value + token_exp.value + token_sign.value + token_1_9.value + token_0_9_plus.value,
                                     token_q.lenght + token_exp.lenght + token_sign.lenght + token_1_9.lenght + token_0_9_plus.lenght)
                    else:
                        return Token(TOKEN_NUMBER,
                                     token_q.value + token_exp.value + token_sign.value + token_1_9.value,
                                     token_q.lenght + token_exp.lenght + token_sign.lenght + token_1_9.lenght)
                else:
                    return token_q
            else:
                return token_q
        else:
            return ERROR
