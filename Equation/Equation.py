import math


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def roots(self):
        D = self.discriminant()
        if D > 0:
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            return x1, x2
        elif D == 0:
            x = -self.b / (2 * self.a)
            return x, x
        else:
            x_real = -self.b / (2 * self.a)
            x_imag = math.sqrt(-D) / (2 * self.a)
            x1 = x_real + x_imag * 1j
            x2 = x_real - x_imag * 1j
            x1 = str(x1).replace('j', 'i')
            x2 = str(x2).replace('j', 'i')
            return  x1, x2

    def __str__(self):
        return 'Root of equation are: {0} '.format(self.roots())

