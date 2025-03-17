from typing import Any

class Singleton:
    instance = None

    @classmethod
    def show(cls, cnf: dict={}, **kwargs) -> Any:
        kwargs = cnf or kwargs

        if cls.instance is None:
            cls.instance = cls(**kwargs)
        return cls.instance