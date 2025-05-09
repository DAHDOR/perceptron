import customtkinter as ctk
from typing import TYPE_CHECKING
from utils import SUB

if TYPE_CHECKING:
    from controller import App

class VectorFrame(ctk.CTkFrame):
    def __init__(self, app: "App", i: int):
        super().__init__(app.ui.vectors_frame)
        self.app = app
        self.i = i
        self.components_entries: list[ctk.CTkEntry] = []

    def setup(self):
        self.label = ctk.CTkLabel(self, text=f"p{self.i}".translate(SUB), fg_color="gray30", corner_radius=6)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.sync()

        self.grid(row=self.i, column=0, padx=5, sticky="ew")

    def sync(self):
        for entry in self.components_entries:
            entry.destroy()
        self.components_entries.clear()
        
        from view.widgets import ComponentEntry
        for j in range(self.app.perceptron.n):
            entry = ComponentEntry(self.app, self.i, j)
            self.components_entries.append(entry)
            entry.setup()