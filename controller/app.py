import numpy as np
from model.perceptron import Perceptron
from typing import TYPE_CHECKING
from model import step, sigmoid, tanh
from tkinter import filedialog
from utils.file import read_weights, read_inputs

if TYPE_CHECKING:
    from view import UI

class App:
    def __init__(self, ui: "UI"):
        self.ui = ui
        self.perceptron = Perceptron()
        self.vectors = [np.zeros(2)]
        self.outputs = [0.0]
        self.m = 1

    def set_n(self, n: int):
        self.perceptron.set_n(n)
        self.ui.perceptron_frame.update_weights()
        self.resize_vectors(n)
    
    def resize_vectors(self, n: int):
        for i in range(len(self.vectors)):
            self.vectors[i] = np.resize(self.vectors[i], n)
            self.ui.vectors_frame.vectors[i].sync()

    def load_weights(self):
        path = filedialog.askopenfilename(
            title="Cargar pesos desde archivo",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )

        if path:
            try:
                weights = np.loadtxt(path, delimiter=',')
                self.perceptron.set_weights(weights)
                self.ui.perceptron_frame.update_weights()
                self.resize_vectors(self.perceptron.n)
                self.ui.vectors_frame.sync()
                self.ui.perceptron_frame.n_entry.delete(0, "end")
                self.ui.perceptron_frame.n_entry.insert(0, str(self.perceptron.n))
            except ValueError as e:
                print(f"Error al cargar los pesos: {e}")

    def load_inputs(self):
        path = filedialog.askopenfilename(
            title="Cargar inputs desde archivo",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )

        if path:
            try:
                inputs = np.loadtxt(path, delimiter=',')
                for input in inputs:
                    if len(input) != self.perceptron.n:
                        raise ValueError(f"El input {input} no tiene la dimensión correcta")
                self.vectors = []
                self.outputs = []
                for input in inputs:
                    self.vectors.append(input)
                self.m = len(self.vectors)
                self.outputs = [0.0] * self.m
                self.ui.menu_frame.m_entry.delete(0, "end")
                self.ui.menu_frame.m_entry.insert(0, str(self.m))
                self.ui.vectors_frame.sync()
                self.ui.output_frame.sync()
            except ValueError as e:
                print(f"Error al cargar los inputs: {e}")
    
    def set_m(self, m: int):
        if m > self.m:
            for i in range(self.m, m):
                self.vectors.append(np.zeros(self.perceptron.n))
                self.outputs.append(self.perceptron.w[0])
        elif m < self.m:
            self.vectors = self.vectors[:m]
            self.outputs = self.outputs[:m]
        else:
            return
        self.m = m
        self.ui.vectors_frame.sync()
        self.ui.output_frame.sync()

    def set_activation_function(self, activation_function: str):
        self.perceptron.set_activation_function({
            "Step": step,
            "Sigmoid": sigmoid,
            "Tanh": tanh
        }[activation_function])
    
    def run(self):
        for i in range(len(self.vectors)):
            self.outputs[i] = self.perceptron.predict(self.vectors[i])
            self.ui.output_frame.outputs[i].sync()