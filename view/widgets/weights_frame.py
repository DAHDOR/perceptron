import customtkinter as ctk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.app import App

class WeightsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master: "App"):
        super().__init__(master, label_text="Pesos")
        self.app = master
        self.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5,10))
        self.create_widgets()

    def create_widgets(self):
        self.weights = []

        self.weights.append((ctk.CTkLabel(self, text="Bias"), ctk.CTkEntry(self, width=100)))

        for i in range(self.app.perceptron.n):
            self.weights.append((ctk.CTkLabel(self, text=f"Peso {i+1}"), ctk.CTkEntry(self, width=100)))