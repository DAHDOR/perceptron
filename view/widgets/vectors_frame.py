import customtkinter as ctk
from typing import TYPE_CHECKING
from .ctk_xyframe import CTkXYFrame

if TYPE_CHECKING:
    from controller import App

class VectorsFrame(CTkXYFrame):
    def __init__(self, app: "App"):
        super().__init__(app.ui)
        self.app = app
        from view.widgets import VectorFrame
        self.vectors: list[VectorFrame] = []

    def setup(self):
        self.sync()
        self.grid(row=0, column=1, padx=(10,0), pady=10, sticky="nsew", rowspan=2)

    def sync(self):
        for vector_frame in self.vectors:
            vector_frame.destroy()
        self.vectors.clear()

        from view.widgets import VectorFrame
        for i in range(len(self.app.vectors)):
            vector_frame = VectorFrame(self.app, i)
            self.vectors.append(vector_frame)
            vector_frame.setup()