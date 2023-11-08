__all__ = ["graphs"]

import structs.graphs

class SimpleStack:
    def __init__(self) -> None:
        self._array = []
    
    def __str__(self) -> str:
        return f"Stack(top={self.peek()}, size={self.size()})"

    def push(self, val) -> None:
        self._array.append(val)
    
    def peek(self):
        return self._array[-1]

    def pop(self):
        if len(self._array) > 0: return self._array.pop(-1)
        else: return False
    
    def size(self) -> int:
        return len(self._array)