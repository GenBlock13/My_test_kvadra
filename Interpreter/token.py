TOKEN_EMPTY = 0
TOKEN_SIGN = 1
TOKEN_INTEGER = 2
TOKEN_DOT = 3
TOKEN_EXP = 4
TOKEN_NAN = 5
TOKEN_INF = 6

STR_EMPTY = 'empty'
STR_SIGN = 'sign'
STR_INTEGER = 'integer'
STR_DOT = 'dot'
STR_EXP = 'exp'
STR_NAN = 'nan'
STR_INF = 'inf'


class Token:
    def __init__(self, type, value, lenght):
        self.type = type
        self.value = value
        self.lenght = lenght

    def __str__(self):
        result = ""
        if self.type == TOKEN_EMPTY:
            result += STR_EMPTY + ': '
        elif self.type == TOKEN_SIGN:
            result += STR_SIGN + ': '
        elif self.type == TOKEN_INTEGER:
            result += STR_INTEGER + ': '
        elif self.type == TOKEN_DOT:
            result += STR_DOT + ': '
        elif self.type == TOKEN_EXP:
            result += STR_EXP + ': '
        elif self.type == TOKEN_NAN:
            result += STR_NAN + ': '
        elif self.type == TOKEN_INF:
            result += STR_INF + ': '
        result += self.value
        return result

    def empty(self):
        self.type = TOKEN_EMPTY
        self.value = ''
        self.lenght = 0
