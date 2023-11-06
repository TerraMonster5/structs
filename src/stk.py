import tkinter as tk

class ToolBar(tk.Menu):
    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)

    def add(self, kind: str, cnf={}, **kwargs):
        kwargs = cnf or kwargs
        if kind == "cascade":
            if "name" in kwargs.keys():
                setattr(self, kwargs["name"], ToolBar(self, **kwargs["menukw"]))
                super().add("cascade", menu=getattr(self, kwargs["name"]), **kwargs["cascadekw"])
            else:
                raise TypeError
        else:
            super().add(kind, **kwargs)

    def add_cascade(self, name: str, cnf={}, **kwargs):
        kwargs = cnf or kwargs
        if name in ToolBar.__dict__.keys():
            raise Exception
        else:
            self.add("cascade", name=name, **kwargs)
    
    def insert(self, index, kind: str, cnf={}, **kwargs):
        kwargs = cnf or kwargs
        if kind == "cascade":
            if "name" in kwargs.keys():
                setattr(self, kwargs["name"], ToolBar(self, **kwargs["menukw"]))
                super().insert(index, "cascade", menu=getattr(self, kwargs["name"]), **kwargs["cascadekw"])
            else:
                raise TypeError
        else:
            super().insert(index, kind, **kwargs)
    
    def insert_cascade(self, index, name: str, cnf={}, **kwargs):
        kwargs = cnf or kwargs
        if name in ToolBar.__dict__.keys():
            raise Exception
        else:
            self.insert(index, "cascade", name=name, **kwargs)