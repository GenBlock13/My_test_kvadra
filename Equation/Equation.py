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
            return x, None
        else:
            x_real = -self.b / (2 * self.a)
            x_imag = math.sqrt(-D) / (2 * self.a)
            x1 = x_real + x_imag * 1j
            x2 = x_real - x_imag * 1j
            return None, x1, x2
        from math import sqrt
        from cmath import sqrt

        def solve_linear(b, c):
            if b == 0 and c == 0:
                linear_root = "Many roots"
                return linear_root
            if b == 0:
                linear_root = "Can't be solved"
                return linear_root
            else:
                linear_root = (-c / b)
            return linear_root

        def solve_discrim(a, b, c):
            dscrm = b * b - 4 * a * c
            x1 = 0
            x2 = 0
            if dscrm < 0:
                x1 = str((-b - sqrt(dscrm)) / (2 * a))
                x2 = str((-b + sqrt(dscrm)) / (2 * a))
                x1 = x1.replace('j', 'i')
                x2 = x2.replace('j', 'i')
                return x1, x2
            elif dscrm == 0:
                x1 = (-b) / (2 * a)
                x2 = (-b) / (2 * a)
                return x1, x2
            else:
                x1 = ((-b) - dscrm ** 0.5) / (2 * a)
                x2 = ((-b) + dscrm ** 0.5) / (2 * a)
                return x1, x2

        def solve_equation(a, b, c):
            if a == 0:
                return solve_linear(b, c)
            else:
                return solve_discrim(a, b, c)


class QuadraticOutput:
    def __init__(self, roots):
        self.roots = roots

    def __str__(self):
        if self.roots[0] is not None:
            x1, x2 = self.roots
            return f"The roots are {x1:.2f} and {x2:.2f}."
        else:
            x = self.roots[1]
            return f"The root is {x:.2f}."