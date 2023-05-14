
class BigNumber:
    def __init__(self, value):
        self.x = value

    def __add__(self, y):
        return self.x + y

    def __radd__(self, y):
        return self.x + y

    def __iadd__(self, y):
        self.x += y
        return self

    def __sub__(self, y):
        return self.x - y

    def __rsub__(self, y):
        return self.x - y

    def __isub__(self, y):
        self.x -= y
        return self

    def __mul__(self, y):
        return self.x * y

    def __rmul__(self, y):
        return self.x * y

    def __imul__(self, y):
        self.x *= y
        return self

    def __truediv__(self, y):
        return self.x / y

    def __rtruediv__(self, y):
        return y/self.x

    def __itruediv__(self, y):
        self.x /= y
        return self


c = BigNumber(100)
d = BigNumber(50)
print(c / 50)
print(c - 50)

print(c/d)
print(d/d)