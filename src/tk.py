import tkinter as tk

class ToolBar(tk.Menu):
    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)

    def add(self, kind, cnf={}, **kwargs):
        kwargs = cnf or kwargs
        if kind == "cascade":
            if "name" in kwargs.keys():
                setattr(self, kwargs["name"], ToolBar(self, **kwargs["menukw"]))
                super().add("cascade", menu=getattr(self, kwargs["name"]), **kwargs["cascadekw"])
            else:
                raise TypeError
        else:
            super().add(kind, **kwargs)