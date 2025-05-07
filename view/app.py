import customtkinter as ctk
from model import Perceptron

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Perceptron")
        self.perceptron = Perceptron(2, 0.5, [0.2, 0.3])
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.perceptron_config_button = ctk.CTkButton(self, text="Configurar Perceptrón", command=self.open_perceptron_config)

    def open_perceptron_config(self):
        # TODO: Open the perceptron configuration window
        pass