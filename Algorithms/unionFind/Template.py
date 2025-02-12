class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x) # initialize the parent of the node to itself

        if x != self.parent[x]: # if the node is not the parent of itself
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x] # return the parent of the node


    def union(self, x: int, y: int) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)


