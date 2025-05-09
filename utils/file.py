import numpy as np

def read_weights(path: str) -> np.ndarray:
    array = np.loadtxt(path, delimiter=',')
    return array

def read_inputs(path: str) -> np.ndarray:
    return np.loadtxt(path, delimiter=',')