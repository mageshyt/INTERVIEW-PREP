from typing import List
from collections import defaultdict , deque
class Solution:
    #Function to detect cycle in an undirected graph.
    # bfs solution
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited=set()
        q=deque() # (node,parent)

        for i in range(V):
            if i not in visited:
                q.append((i,-1))
                visited.add(i)
                while q:
                    node,parent=q.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            q.append((neighbor,node))
                            visited.add(neighbor)
                        elif neighbor != parent:
                            return True
        return False

    # dfs soltion
    def isCycle2(self,V,adj):
        visited=set()

        def dfs(node,parent):
            # if the node is already visited and not the parent of the current node
            if node in visited and node != parent:
                return True

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor != parent and dfs(neighbor,node):
                    return True

            return False

        for i in range(V):
            if i not in visited:
                if dfs(i,-1):
                    return True

        return False


print(Solution().isCycle(4,[[0,1],[1,2],[2,3],[3,0]])) # True
            

        



