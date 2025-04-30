import numpy as np

class Perceptron:
    def __init__(self, n, bias=0, weights=None):
        self.n: int = n
        self.bias: float = bias
        self.weights: np.ndarray = np.random.rand(n) if weights is None else weights

    def sum(self, inputs: np.ndarray) -> float: return np.dot(inputs, self.weights) + self.bias