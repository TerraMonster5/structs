from typing import Any

class Singleton:
    def __init__(self, decorated) -> None:
        self.__decorated = decorated
        if not "instance" in self.__decorated.__dict__:
            self.__decorated.instance = None

    def __call__(self) -> Any:
        if self.__decorated.instance is None:
            self.__decorated.instance = self.__decorated()
            return self.__decorated.instance
        else:
            return self.__decorated.instance
    
    def __instancecheck__(self, instance: Any) -> bool:
        return isinstance(instance, self.__decorated)