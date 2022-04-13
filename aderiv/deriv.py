from __future__ import annotations
import numpy as np
from aderiv import Dual


def deriv(f: callable, x: float, xp: float = 1.):
    """二重数を用いて自動微分を計算。

    Args:
        f (callable): 微分したい有理関数
        x (float): 微分したい点
        xp (float, optional): 二重数の係数(いじらなくてもいいけどいじると数値的によくなったりすることがあるかも？). Defaults to 1..

    Returns:
        _type_: _description_
    """
    dfd = f(Dual(x, xp)) - f(Dual(x, 0))
    assert np.isclose((df := Dual.undual(dfd))[0], 0)
    return df[1] / xp