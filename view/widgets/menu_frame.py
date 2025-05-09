import customtkinter as ctk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import App

class MenuFrame(ctk.CTkFrame):
    def __init__(self, app: "App"):
        super().__init__(app.ui)
        self.app = app

    def setup(self):
        self.grid(row=1, column=0, padx=(10, 0), pady=(0, 10), sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        
        self.load_weights_button = ctk.CTkButton(self, text="Cargar pesos desde archivo", command=self.load_weights)
        self.load_weights_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew", columnspan=2)

        self.load_inputs_button = ctk.CTkButton(self, text="Cargar inputs desde archivo", command=self.load_inputs)
        self.load_inputs_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew", columnspan=2)

        self.m_label = ctk.CTkLabel(self, text="# de inputs")
        self.m_label.grid(row=2, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")

        self.m_entry = ctk.CTkEntry(self)
        self.m_entry.insert(0, str(self.app.m))
        self.m_entry.grid(row=2, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.m_entry.bind("<Return>", self.set_m)
        self.m_entry.bind("<FocusOut>", self.set_m)

        self.activation_function_label = ctk.CTkLabel(self, text="Función de Act.")
        self.activation_function_label.grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")

        self.activation_function = ctk.CTkOptionMenu(self, values=["Step", "Sigmoid", "Tanh"], command=self.set_activation_function)
        self.activation_function.grid(row=3, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.activation_function.set("Step")

        self.run_button = ctk.CTkButton(self, text="Ejecutar", command=self.run)
        self.run_button.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew", columnspan=2)

    def load_weights(self, event=None):
        self.app.load_weights()

    def load_inputs(self, event=None):
        self.app.load_inputs()

    def set_m(self, event=None):
        try:
            m = int(self.m_entry.get())
            if m < 1:
                raise ValueError
            self.app.set_m(m)
        except ValueError:
            self.m_entry.delete(0, ctk.END)
            self.m_entry.insert(0, str(self.app.m))

    def set_activation_function(self, value: str):
        self.app.set_activation_function(value)

    def run(self):
        self.app.run()