from Interpreter.token_z import *
from Interpreter.token_dot import *
from Interpreter.token_0_9_plus import *
from Interpreter.token_sign import *
from Interpreter.token import *


class Tokenizer_Q(TokenizerInterface):
    def __init__(self):
        super().__init__()
        self.tokenizer_z = Tokenizer_Z()
        self.tokenizer_dot = Tokenizer_dot()
        self.tokenizer_0_9_plus = Tokenizer0_9_plus()
        self.tokenizer_sign = Tokenizer_sign()

    def interpret(self, string, position):
        if not self._check_bounds(string, position):
            return ERROR

        current = position
        token_z = self.tokenizer_z.interpret(string, current)
        if token_z.type != TOKEN_EMPTY:
            current += token_z.lenght
            token_dot = self.tokenizer_dot.interpret(string, current)

            if token_dot.type != TOKEN_EMPTY:
                current += token_dot.lenght
                token_frac = self.tokenizer_0_9_plus.interpret(string, current)

                if token_frac.type != TOKEN_EMPTY:
                    return Token(TOKEN_NUMBER, token_z.value + token_dot.value + token_frac.value,
                                 token_z.lenght + token_dot.lenght + token_frac.lenght)
                else:
                    return Token(TOKEN_NUMBER, token_z.value + token_dot.value,
                                 token_z.lenght + token_dot.lenght)
            else:
                return token_z
        else:
            token_sign = self.tokenizer_sign.interpret(string, current)
            if token_sign != TOKEN_EMPTY:
                current += 1

            token_dot = self.tokenizer_dot.interpret(string, current)
            if token_dot.type != TOKEN_EMPTY:
                current += token_dot.lenght
                token_frac = self.tokenizer_0_9_plus.interpret(string, current)

                if token_frac.type != TOKEN_EMPTY:
                    return Token(TOKEN_NUMBER, token_sign.value + token_dot.value + token_frac.value,
                                 token_sign.lenght + token_dot.lenght + token_frac.lenght)
                else:
                    return ERROR
            else:
                return ERROR
