import tkinter as tk

class ToolBar(tk.Menu):
    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)

    def add(self, kind: str, cnf={}, **kwargs):
        kwargs = cnf or kwargs

        if kind == "cascade":
            if "menukw" not in kwargs.keys():
                kwargs["menukw"] = {}
            if "cascadekw" not in kwargs.keys():
                kwargs["cascadekw"] = {}

            if "name" in kwargs.keys():
                setattr(self, kwargs["name"], ToolBar(self, **kwargs["menukw"]))
                getattr(self, kwargs["name"]).__name__ = kwargs["name"]
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

    def insert(self, index: int, kind: str, cnf={}, **kwargs):
        kwargs = cnf or kwargs

        if kind == "cascade":
            if "menukw" not in kwargs.keys():
                kwargs["menukw"] = {}
            if "cascadekw" not in kwargs.keys():
                kwargs["cascadekw"] = {}

            if "name" in kwargs.keys():
                setattr(self, kwargs["name"], ToolBar(self, **kwargs["menukw"]))
                getattr(self, kwargs["name"]).__name__ = kwargs["name"]
                super().insert(index, "cascade", menu=getattr(self, kwargs["name"]), **kwargs["cascadekw"])
            else:
                raise TypeError
        else:
            super().insert(index, kind, **kwargs)

    def insert_cascade(self, index: int, name: str, cnf={}, **kwargs):
        kwargs = cnf or kwargs

        if name in ToolBar.__dict__.keys():
            raise Exception
        else:
            self.insert(index, "cascade", name=name, **kwargs)

    def delete(self, index1: int, index2: int | None=None):
        if index2 is None:
            index2 = index1

        for i in range(index1, index2+1):
            if self.type(i) == tk.CASCADE:
                delattr(self, self.nametowidget(self.entrycget(i, "menu")).__name__)
        
        super().delete(index1, index2)