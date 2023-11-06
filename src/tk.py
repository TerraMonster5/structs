import tkinter as tk

class ToolBar(tk.Menu):
    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)

    def add(self, kind, **kwargs):
        if kind == "cascade":
            if "name" in kwargs.keys():
                self.add_cascade(kwargs["name"], kwargs["label"], **kwargs)
            else:
                raise TypeError
        else:
            super().add(kind, **kwargs)

    def add_cascade(self, name: str, *, menukwargs: dict, cascadekwargs: dict) -> None:
        if name in ToolBar.__dict__.keys():
            raise Exception
        else:
            setattr(self, name, ToolBar(self, **menukwargs))
            super().add_cascade(menu=getattr(self, name), **cascadekwargs)

    def insert_cascade(self, index: int, name: str, *, menukwargs: dict, cascadekwargs: dict) -> None:
        if name in ToolBar.__dict__.keys():
            raise Exception
        else:
            setattr(self, name, ToolBar(self, **menukwargs))
            super().insert_cascade(index, menu=getattr(self, name), **cascadekwargs)
    
    def delete(self, index1, index2=None):
        pass