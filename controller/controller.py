class Controller:
    def __init__(self):
        from model import Perceptron
        import numpy as np
        self.perceptron = Perceptron()
        self.vectors = [np.array([1,1])]

    