import customtkinter as ctk
from typing import TYPE_CHECKING
from utils import SUB

if TYPE_CHECKING:
    from controller import App

class OutputItem(ctk.CTkFrame):
    def __init__(self, app: "App", i: int):
        super().__init__(app.ui.output_frame)
        self.app = app
        self.i = i

    def setup(self):
        self.grid(row=self.i, column=0, padx=10, pady=5, sticky="w")
        self.label = ctk.CTkLabel(self, text=f"p{self.i}".translate(SUB) + f" -> {self.app.outputs[self.i]}")
        self.label.grid(row=0, column=0, padx=5, sticky="w")

    def sync(self):
        self.label.configure(text=f"p{self.i}".translate(SUB) + f" -> {self.app.outputs[self.i]}")