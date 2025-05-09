import customtkinter as ctk
from typing import TYPE_CHECKING
from view.widgets.weight_item import WeightItem

if TYPE_CHECKING:
    from controller import App

class PerceptronFrame(ctk.CTkScrollableFrame):
    def __init__(self, app: "App"):
        super().__init__(app.ui, width=150, label_text="Perceptrón")
        self.app = app

    def setup(self):
        self.n_frame = ctk.CTkFrame(self)
        self.n_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.n_frame.grid_columnconfigure(0, weight=1)
        self.n_frame.grid_columnconfigure(1, weight=3)
        
        self.n_label = ctk.CTkLabel(self.n_frame, text="n")
        self.n_label.grid(row=0, column=0, padx=5, sticky="ew")

        self.n_entry = ctk.CTkEntry(self.n_frame)
        self.n_entry.grid(row=0, column=1, padx=5, sticky="ew")
        self.n_entry.insert(0, str(self.app.perceptron.n))

        n_validate_command = self.app.ui.register(self.validate_n_entry)
        self.n_entry.configure(validate="focusout", validatecommand=(n_validate_command, "%P"))
        
        self.weight_items: list[WeightItem] = []
        
        self.update_weights()

        self.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)


    def validate_n_entry(self, new: str) -> bool:
        try:
            n = int(new)
            if n < 1:
                raise ValueError('"n" debe ser mayor que 0')
            if n != self.app.perceptron.n:
                self.app.set_n(n)
            return True
        except ValueError:
            self.n_entry.delete(0, "end")
            self.n_entry.insert(0, str(self.app.perceptron.n))
            return False
    
    def update_weights(self):
        for weight_item in self.weight_items:
            weight_item.destroy()
        self.weight_items.clear()
        for i in range(self.app.perceptron.n + 1):
            weight_item = WeightItem(self.app, i)
            self.weight_items.append(weight_item)