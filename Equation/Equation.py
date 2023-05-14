from math import sqrt


class Quad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_a(self):
        if self.a == 0:
            print('Solve it linear')
        return self.a

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve_linear(self):
        if self.c == 0 and self.b == 0:
            self.x = "MANY ROOTS"
            return self.x

        elif self.b != 0 and c == 0:
            self.x = 0
            return 'ROOT is: {0}'.format(self.x)

        elif self.b != 0:
            self.x = - self.c / self.b
            return 'ROOT is: {0:.3f}'.format(self.x)

        else:
            self.x = 'NO ROOTS'
            return self.x

    def solve_quadr(self):
        D = self.discriminant()
        if D > 0:
            x1 = (-self.b + sqrt(D)) / (2 * self.a)
            x2 = (-self.b - sqrt(D)) / (2 * self.a)
            return 'First ROOT: {0:.3f}, Second ROOT: {1:.3f}'.format(x1, x2)
        elif D == 0:
            x = -self.b / (2 * self.a)
            return x, x
        elif D < 0:
            x_real = -self.b / (2 * self.a)
            x_imag = sqrt(-D) / (2 * self.a)
            return 'First ROOT: {0:.4f} + {1:.4f}i, Second ROOT: {0:.4f} - {1:.4f}i'.format(x_real, x_imag)

    def __str__(self):
        if self.a == 0:
            return 'Result of equation -  {0}'.format(self.solve_linear())
        else:
            return 'Result of equation -  {0}'.format(self.solve_quadr())


a, b, c = list(map(float, input().split(' ')))

n1 = Quad(a, b, c)
if n1.a == 0:
    n1.solve_linear()
else:
    n1.solve_quadr()

print(n1)