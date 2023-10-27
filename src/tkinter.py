import tkinter as tk
from tkinter import ttk

class ToolBar(tk.Menu):
    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)

    def addChild(self, itemType: str="menu", name: str="", **kwargs) -> None:
        if itemType == "menu":
            setattr(self, name, ToolBar(self, **kwargs))
            self.add_cascade(label=name, menu=getattr(self, name))