from __future__ import annotations
import numpy as np
from aderiv import Dual


def deriv(f: callable, x: float, xp: float = 1.):
    dfd = f(Dual(x, xp)) - f(Dual(x, 0))
    assert np.isclose((df := Dual.undual(dfd))[0], 0)
    return df[1] / xp