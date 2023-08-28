from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

        

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__

    
arr = []
def addToL(value: Node) -> list[Node]:
    if not value in arr:
        arr.append(value)

class Graph:
    def __init__(self, root: Node):
        self._root = root

    def rec_dfs(self) -> list[Node]:
        if len(self._root.outbound) <= 0:
            if len(self._root.inbound) == 0:
                addToL(self._root)
                return arr
            return
        addToL(self._root)
        for i in range(len(self._root.outbound)):
            if not self._root.outbound[i] in arr:
                addToL(self._root.outbound[i])
                gr = Graph(self._root.outbound[i])
                gr.rec_dfs()
        return arr
        
    def rec_bfs(self) -> list[Node]:
        if len(self._root.outbound) <= 0:
            if len(self._root.inbound) == 0:
                addToL(self._root)
                return arr
            return
        addToL(self._root)
        tempNodeList = []
        for i in range(len(self._root.outbound)):
            if not self._root.outbound[i] in arr:
                addToL(self._root.outbound[i])
                tempNodeList.append(self._root.outbound[i])
        for v in range(len(tempNodeList)):
                gr = Graph(tempNodeList[v])
                gr.rec_bfs()
        return arr    
    
    def dfs(self) -> list[Node]:
        global arr
        arr = []
        return self.rec_dfs()

    def bfs(self) -> list[Node]:
        global arr
        arr = []
        return self.rec_bfs()
