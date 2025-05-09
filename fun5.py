import math
from math import factorial


def H(factors, x):
    result = factors[0]
    for i in range(1, len(factors)):
        result = result * x + factors[i]
    return result


def L(x: float, n: int):
    arr = [1, x-1]
    if n == 0 or n == 1:
        return arr[n]
    else:
        for i in range(1, n):
            arr.append((arr[i] * (x - 1 - (2 * i))) - (i ** 2 * arr[i - 1]))
        return arr[n]


def calculate(f, w, x, nodes, i):
    res = 0
    for n in range(0, nodes):
        res += w[n] * f(x[n]) * L(x[n], i)
    return res / (factorial(i) ** 2)


def error(f, w, x, factors, nodes, n):
    err = 0
    F = [0]*nodes
    for i in range(nodes):
        for j in range(n):
            F[i] += factors[j] * L(x[i], j)
    for i in range(nodes):
        err += w[i] * ((f(x[i]) - F[i]) ** 2)
    return math.sqrt(err)