import customtkinter as ctk
from controller import App
from view.widgets import PerceptronFrame, VectorsFrame, OutputFrame
from view.widgets import MenuFrame

class UI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Perceptron")
        self.app = App(self)
        self.geometry("800x600")
        self.setup()

    def setup(self):

        self.output_frame = OutputFrame(self.app)

        self.perceptron_frame = PerceptronFrame(self.app)
        self.perceptron_frame.setup()

        self.menu_frame = MenuFrame(self.app)
        self.menu_frame.setup()

        self.vectors_frame = VectorsFrame(self.app)
        self.vectors_frame.setup()

        self.output_frame.setup()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)