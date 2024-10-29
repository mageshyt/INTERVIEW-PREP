class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def union(self,x:int,y:int)->None:
        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def find(self,x:int)->int:
        self.parent.setdefault( x, x)

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


