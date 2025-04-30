def step(x: float) -> int: return 1 if x > 0 else 0

def linear(m: float, x: float, b: float) -> float: return m * x + b

def sigmoid(x: float) -> float:
    from numpy import exp
    return 1 / (1 + exp(-x))

def tanh(x: float) -> float:
    from numpy import tanh
    return tanh(x)