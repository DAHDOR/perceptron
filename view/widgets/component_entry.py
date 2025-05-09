import customtkinter as ctk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import App

class ComponentEntry(ctk.CTkEntry):
    def __init__(self, app: "App", i: int, j: int):
        super().__init__(app.ui.vectors_frame.vectors[i], width=50)
        self.app = app
        self.i = i
        self.j = j

    def setup(self):
        self.insert(0, str(self.app.vectors[self.i][self.j]))
        self.grid(row=0, column=self.j+1, padx=5, pady=5)
        self.bind("<Return>", self.update_component)
        self.bind("<FocusOut>", self.update_component)
        self.grid(row=0, column=self.j+1, padx=5, sticky="ew")

    def update_component(self, event=None):
        try:
            value = float(self.get())
            self.app.vectors[self.i][self.j] = value
            self.sync()
        except ValueError:
            self.sync()

    def sync(self):
        self.delete(0, "end")
        self.insert(0, str(self.app.vectors[self.i][self.j]))