from typing import Any
from queue import SimpleQueue

class SimpleStack:
    def __init__(self) -> None:
        self._array = []
    
    def __str__(self) -> str:
        return f"Stack(top={self.peek()}, size={self.size()})"

    def push(self, val) -> None:
        self._array.append(val)
    
    def peek(self) -> Any:
        return self._array[-1]

    def pop(self, b: int=0) -> Any | bool:
        if len(self._array) > b: return self._array.pop(-1)
        else: return False
    
    def size(self) -> int:
        return len(self._array)
    
    def empty(self) -> bool:
        return not len(self._array)

class Graph:
    class Vertex:
        def __init__(self, adjacency: dict) -> None:
            self.adjacency = adjacency

        def __str__(self) -> str:
            return f"Vertex({self.adjacency})"
    
    def __init__(self) -> None:
        self.vertices = []
    
    def __str__(self) -> str:
        temp = ", ".join([str(x) for x in self.vertices])
        return f"Graph({temp})"

    def breadth(self, vertex: int, visited: list=[], q: SimpleQueue=SimpleQueue()) -> list:
        if vertex not in visited:
            visited.append(vertex)
        
        for edgeVertex in self.vertices[vertex].adjacency:
            if edgeVertex not in visited:
                q.put_nowait(edgeVertex)
                visited.append(edgeVertex)

        if q.qsize() > 0:
            self.breadth(q.get_nowait(), visited, q)
        
        return visited

    def depth(self, vertex: int, visited: list=[], s: SimpleStack=SimpleStack()) -> list:
        if vertex not in visited:
            visited.append(vertex)
        
        for edgeVertex in self.vertices[vertex].adjacency:
            if edgeVertex not in visited:
                s.push(edgeVertex)
        
        if len(visited) != len(self.vertices):
            self.depth(s.pop(), visited, s)
        
        return visited
    
    def dijkstras(self, currentVertex: int, table=None) -> dict:
        if table is None:
            table = {
                "vertex": self.vertices,
                "distance": [None] * len(self.vertices),
                "visited": [False] * len(self.vertices),
                "previous": [None] * len(self.vertices)
                }
            table["distance"][currentVertex] = 0
            for vertex, cost in table["vertex"][currentVertex].adjacency.items():
                table["distance"][vertex] = cost
                table["previous"][vertex] = 0

        for vertex in table["vertex"][currentVertex].adjacency.keys():
            if not table["visited"][vertex]:
                oldPrevious = table["previous"][vertex]
                table["previous"][vertex] = currentVertex
                dist = table["distance"][table["previous"][vertex]] + table["vertex"][currentVertex].adjacency[vertex]
                if table["distance"][vertex] is None or dist < table["distance"][vertex]:
                    table["distance"][vertex] = dist
                else:
                    table["previous"][vertex] = oldPrevious

        table["visited"][currentVertex] = True

        if False in table["visited"]:
            temp = [None if table["visited"][x] else table["distance"][x] for x in range(0, len(table["distance"]))]
            new = min((val, index) for index, val in enumerate(temp) if val is not None)
            self.dijkstras(new[1], table)

        return table