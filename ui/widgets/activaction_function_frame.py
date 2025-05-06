import customtkinter as ctk

class ActivationFunctionFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.selected = ctk.StringVar(value="Escalonada")
        self.initialize_ui()

    def initialize_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self, text="Función de activación")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.menu = ctk.CTkOptionMenu(
            self,
            variable=self.selected,
            values=["Escalonada", "Lineal", "Sigmoidal", "Tangente Hiperbólica"],
            command=self.on_change,
        )
        self.menu.grid(row=0, column=1, padx=10, pady=10)

    def on_change(self, value):
        print(f"Selected activation function: {value}")
        # TODO
        
    def get_selected_activation_function(self):
        # Return the currently selected activation function
        return self.selected.get()