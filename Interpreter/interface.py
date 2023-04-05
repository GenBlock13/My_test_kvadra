from abc import ABC

class TokenizerInterface(ABC):
    def __init__(self):
        pass

    def interpret(self, string, position):
        pass
