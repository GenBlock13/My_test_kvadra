class BigNumberToken:

    def __init__(self, positive, integer, fraction, exponent):
        self.positive = positive
        self.integer = integer
        self.fraction = fraction
        self.exponent = exponent


BNK_EMPTY_ELEMENT = 0
BNK_MAX_LENGTH = 30


class BigNumberContainer:

    def __init__(self):
        self._max = 0
        self._min = 0
        self._delta = 0
        self._dict = dict()

    def shift_digit(self, shift):
        self._delta = shift
        self._min += shift
        self._max += shift

    def position_to_index(self, position):
        return position - self._delta

    def index_to_position(self, index):
        return index + self._delta

    def __getitem__(self, item):
        item = self.position_to_index(item)
        if item in self._dict:
            return self._dict[item]
        return BNK_EMPTY_ELEMENT


class BigFloat:

    def __init__(self, tokens: BigNumberToken):
        self.positive = tokens.positive
        self._container = BigNumberContainer()
        self._build_from_tokens(tokens)

    def __str__(self):
        result = ''
        if not self.positive:
            result = '-'


