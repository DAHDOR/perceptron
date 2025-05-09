from typing import TYPE_CHECKING
import customtkinter as ctk

if TYPE_CHECKING:
    from controller import App

class OutputFrame(ctk.CTkScrollableFrame):
    def __init__(self, app: "App"):
        super().__init__(app.ui, label_text="Outputs")
        self.app = app
        from view.widgets import OutputItem
        self.outputs: list[OutputItem] = []

    def setup(self):
        self.grid(row=0, column=2, sticky="nsew", padx=(10, 10), pady=10, rowspan=2)
        self.grid_columnconfigure(0, weight=1)
        self.sync()

    def sync(self):
        for item in self.outputs:
            item.destroy()
        self.outputs.clear()
        from view.widgets import OutputItem
        for i in range(len(self.app.vectors)):
            item = OutputItem(self.app, i)
            item.setup()
            self.outputs.append(item)