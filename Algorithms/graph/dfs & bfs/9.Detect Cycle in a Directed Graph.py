#User function Template for python3
from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        visited=set()
        path=set()

        def dfs(node):
            # if the node is already visited and in the path
            if node in path:
                return True

            if node in visited:
                return False

            visited.add(node)
            path.add(node)

            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True


            path.remove(node)

            return False


        for i in range(V):
            if i not in visited:
                if dfs(i):
                    return True

        return False





