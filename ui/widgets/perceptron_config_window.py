from typing import TYPE_CHECKING
import customtkinter as ctk

if TYPE_CHECKING:
    from ui.app import App

class PerceptronConfigWindow(ctk.CTkToplevel):
    def __init__(self, master: "App" = None):
        super().__init__(master)
        self.title("Configuración del Perceptrón")
        self.geometry("400x300")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        from widgets.activaction_function_frame import ActivationFunctionFrame
        self.activation_function_frame = ActivationFunctionFrame(self)