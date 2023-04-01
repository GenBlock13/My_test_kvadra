def solve_linear(b, c):
    if b != 0:
        x = - c / b
        return 'Equation root is {0:.5}'.format(x)
    else:
        if c == 0:
            return 'Any X solves equation'
        else:
            return 'No solution'