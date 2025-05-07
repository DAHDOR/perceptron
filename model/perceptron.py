import numpy as np

class Perceptron:
    def __init__(self, n: int = 1, bias: int = 0, weights: np.ndarray = None) -> None:
        self.n = n
        self.bias = bias
        self.weights = np.random.rand(n) if weights is None else weights

    def sum(self, inputs: np.ndarray) -> float: return np.dot(inputs, self.weights) + self.bias

    def set_n(self, n: int) -> None:
        if n < 1: raise ValueError("N debe ser mayor que 0")
        if n == self.n: return
        elif n < self.n: self.weights = self.weights[:n]
        else: self.weights = np.append(self.weights, np.random.rand(n - self.n))