import pytest
from random import randint, shuffle
import math
import numpy as np
from aderiv import deriv

def test_polynomial():
    for i in range(0, 6):
        f, df = gen_polynomial(i)
        for x in range(-10, 10):
            assert np.isclose(deriv(f, x), df(x))

def test_radical():
    a = 0
    while a == 0:
        f, df = gen_polynomial(5)
        g, dg = gen_polynomial(6)
        a = g(2)
    def f_on_g(x):
        return f(x) / g(x)
    assert np.isclose(deriv(f_on_g, 2), (df(2)*g(2) - f(2)*dg(2)) / (g(2))**2)


def test_others():
    def exp(x, k = 100):
        ans = 0
        for i in range(k):
            ans += (1 / math.factorial(i)) * (x ** i)
        return ans

    def sin(x, k = 100):
        ans = 0
        for i in range(k):
            ans += (((-1) ** i) / math.factorial(2 * i + 1)) * (x ** (2 * i + 1))
        return ans

    def cos(x, k = 100):
        ans = 0
        for i in range(k):
            ans += (((-1) ** i) / math.factorial(2 * i)) * (x ** (2 * i))
        return ans
    assert np.isclose(deriv(exp, 2), exp(2))
    assert np.isclose(deriv(sin, 2), cos(2))
    assert np.isclose(deriv(cos, 2), -sin(2))

def gen_polynomial(deg: int):
    coefs = [randint(0, 10) for _ in range(0, deg + 1)]
    degs = list(range(0, deg + 1))
    shuffle(degs)
    def f(x):
        ans = 0
        for i, d in enumerate(degs):
            ans += coefs[i] * x ** d
        return ans

    def df(x):
        ans = 0
        for i, d in enumerate(degs):
            ans += d * coefs[i] * x ** (d - 1) if d > 0 else 0
        return ans

    return f, df
        