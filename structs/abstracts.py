from typing import Any

class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(type(cls))
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def singleton(cls):
    return _Singleton(cls.__name__, cls.__bases__, dict(cls.__dict__))