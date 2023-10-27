import tkinter as tk

class ToolBar(tk.Menu):
    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)

    def add_cascade(self, name: str, label: str, **kwargs) -> None:
        setattr(self, name, ToolBar(self, **kwargs))
        super().add_cascade(label=label, menu=getattr(self, name))