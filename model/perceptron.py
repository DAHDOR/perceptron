from typing import Callable
from model.activation_functions import step
import numpy as np


class Perceptron:
    def __init__(self, n: int = 2, w: np.ndarray = None, activation_function: Callable = step) -> None:
        self.n = n
        self.w = np.zeros(n + 1) if w is None else w
        self.activation_function = activation_function

    def predict(self, X: np.ndarray) -> float:
        weighed_sum = np.dot(X, self.w[1:]) + self.w[0]
        return self.activation_function(weighed_sum)

    def set_n(self, n: int) -> None:
        self.w = np.resize(self.w, n + 1)
        self.n = n

    def set_weight(self, i: int, w: float) -> None:
        if i < 0 or i >= len(self.w):
            raise IndexError("El índice está fuera de rango")
        self.w[i] = w

    def set_weights(self, w: np.ndarray) -> None:
        if self.n != len(w) - 1:
            self.n = len(w) - 1
        self.w = w

    def set_activation_function(self, activation_function: Callable) -> None:
        self.activation_function = activation_function