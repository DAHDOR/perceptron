import customtkinter as ctk
from typing import TYPE_CHECKING
from utils import SUB

if TYPE_CHECKING:
    from controller import App

class WeightItem(ctk.CTkFrame):
    def __init__(self, app: "App", i: int) -> None:
        super().__init__(app.ui.perceptron_frame)
        self.app = app
        self.i = i
        self.setup()

    def setup(self):
        self.label = ctk.CTkLabel(self, text=f"w{self.i}".translate(SUB))
        self.label.grid(row=0, column=0, padx=5, sticky="w")

        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=0, column=1, padx=5, sticky="ew")
        self.sync()
        self.entry.bind("<Return>", self.validate_entry)
        self.entry.bind("<FocusOut>", self.validate_entry)

        self.grid(row=self.i+1, column=0, padx=5, pady=5, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

    def validate_entry(self, event=None):
        try:
            w = float(self.entry.get())
            self.app.perceptron.set_weight(self.i, w)
            self.sync()
        except ValueError:
            self.sync()

    def sync(self):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(self.app.perceptron.w[self.i]))