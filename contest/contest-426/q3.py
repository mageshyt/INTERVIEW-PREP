
from collections import deque,defaultdict
from typing import List
class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]],k) -> List[int]:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        for src,dst in edges1:
            adj1[src].append(dst)
            adj1[dst].append(src)

        for src,dst in edges2:
            adj2[src].append(dst)
            adj2[dst].append(src)


        res = [0]*len(edges1)

        for i in range(len(edges1)):
            res[i] = self.bfs(i,adj1,k-1)

        goldenNode=0

        for i in range(len(edges2)):
            goldenNode = max(goldenNode,self.bfs(i,adj2,k-1))



        
        return [num+goldenNode for num in res]



    def bfs(self,src,adj,k):
        q=deque([(src,0)])
        cnt,dist=0,0

        visited=set()

        while q and dist <= k:
            node,dist = q.popleft()

            if node in visited:
                continue

            visited.add(node)

            cnt += 1

            for neighbor in adj[node]:
                q.append((neighbor,dist+1))

        return cnt


s=Solution()
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2

print(s.maxTargetNodes(edges1,edges2,k)) #[4, 5, 5, 5]

