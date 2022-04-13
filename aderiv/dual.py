from __future__ import annotations
import numpy as np


class Dual:
    def __init__(
        self, 
        a: float,
        b: float
    ) -> None:
        """二重数を定義

        Args:
            a (float): 実部
            b (float): 二重部(？)
        """
        self.a = float(a)
        self.b = float(b)
        self.value = _make_dual(a, b)

    def __getitem__(self, i):
        return self.value[i]

    def __str__(self) -> str:
        return np.matrix.__str__(self.value)
    
    def __repr__(self) -> str:
        return np.matrix.__repr__(self.value)

    @staticmethod
    def analyze(d: Dual or np.matrix) -> bool:
        """二重数かどうか判定する

        Args:
            d (Dual or np.matrix): 判定したいオブジェクト

        Returns:
            bool: 正誤
        """
        cond1 = np.isclose(d[0, 1], - d[1, 0])
        cond2 = np.isclose(d[0, 0] + d[1, 0], d[0, 1] + d[1, 1])
        return cond1 and cond2

    @staticmethod
    def undual(d: Dual or np.matrix) -> tuple(float, float):
        """二重数(行列表示)をタプルに変換

        Args:
            d (Dual or np.matrix): 二重数

        Raises:
            ValueError: 二重数じゃないと怒る

        Returns:
            tuple(float, float): 二重数の2つ組
        """
        if not (Dual.analyze(d)):
            raise ValueError(f'input is not dual number.')
        else:
            return (d[0, 0] + d[1, 0], d[0, 1])

    @staticmethod
    def from_value(value: np.matrix) -> Dual:
        """np.matrixから二重数を作る

        Args:
            value (np.matrix): 行列

        Raises:
            ValueError: 二重数じゃないと怒る

        Returns:
            Dual: 作成された二重数
        """
        if Dual.analyze(value):
            return Dual(*Dual.undual(value))
        else:
            raise ValueError(f'input is not dual number.')

    @staticmethod
    def from_real(value: int or float) -> Dual:
        return Dual(float(value), 0) 

    @staticmethod
    def sanitize(value: Dual or int or float) -> Dual:
        return Dual.from_real(value) if isinstance(value, int) or isinstance(value, float) else value

    def __add__(self, other: Dual or int or float) -> Dual:
        other = Dual.sanitize(other)
        return Dual.from_value(self.value + other.value)

    def __radd__(self, other: int or float) -> Dual:
        other = Dual.sanitize(other)
        return Dual.from_value(self.value + other.value)

    def __sub__(self, other: Dual or int or float) -> Dual:
        other = Dual.sanitize(other)
        return Dual.from_value(self.value - other.value)

    def __rsub__(self, other: int or float) -> Dual:
        other = Dual.sanitize(other)
        return Dual.from_value(other.value - self.value)

    def __mul__(self, other: Dual or int or float) -> Dual:
        other = Dual.sanitize(other)
        return Dual.from_value(self.value * other.value)

    def __rmul__(self, other: int or float) -> Dual:
        other = Dual.sanitize(other)
        return Dual.from_value(self.value * other.value)

    def __pow__(self, other: int) -> Dual:
        return Dual.from_value(self.value ** other)
    
    def __truediv__(self, other: Dual or int or float) -> Dual:
        other = Dual.sanitize(other)
        return self * Dual(other.a / (other.a ** 2), - other.b / (other.a ** 2))
    
    def __rtruediv__(self, other: int or float) -> Dual:
        return other * Dual(self.a / (self.a ** 2), - self.b / (self.a ** 2))
        

def _make_dual(a: float, b: float): 
    return np.diag([a, a]) + np.diag([b, b]) * np.matrix([[1,1],[-1, -1]])