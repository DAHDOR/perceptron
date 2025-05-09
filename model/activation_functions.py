import numpy as np

def step(x: float) -> int: return 1 if x > 0 else 0

def sigmoid(x: float) -> float: return 1 / (1 + np.exp(-x))

def tanh(x: float) -> float: return np.tanh(x)