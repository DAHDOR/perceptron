import numpy as np
import pytest
from perceptron import Perceptron

def test_sum_and_step():
    weights = np.array([1.0, -1.0, 0.5])
    bias = 0.2
    p = Perceptron(n=3, bias=bias, weights=weights)
    inputs = np.array([2.0, 1.0, -1.0])
    # sum = 2*1 + 1*-1 + (-1)*0.5 + 0.2 = 2 - 1 - 0.5 + 0.2 = 0.7
    assert p.sum(inputs) == pytest.approx(0.7)
    # step activation
    assert p.step(0.7) == 1
    assert p.step(0.0) == 0
    assert p.step(-0.1) == 0

def test_linear():
    p = Perceptron(n=1)
    assert p.linear(2.0, 3.0, -1.0) == pytest.approx(2.0 * 3.0 + -1.0)

def test_sigmoid_and_tanh():
    p = Perceptron(n=1)
    # sigmoid at 0
    assert p.sigmoid(0.0) == pytest.approx(0.5)
    # extreme values
    assert p.sigmoid(100) > 0.99
    assert p.sigmoid(-100) < 0.01
    # tanh
    assert p.tanh(0.0) == pytest.approx(0.0)
    assert p.tanh(2.0) == pytest.approx(np.tanh(2.0))
    assert p.tanh(-2.0) == pytest.approx(np.tanh(-2.0))
