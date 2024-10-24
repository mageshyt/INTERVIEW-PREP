
from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n # -1 means uncolored, 0 and 1 are the two colors


        for start in range(n):
            # if the node is not yet colored 

            if color[start] ==-1:
                # start a BFS from this node
                queue=deque([start])
                color[start]=0

                while queue:
                    node=queue.popleft()

                    # try to color all neighbours with the opposite color

                    for neighbour in graph[node]:
                        # color the neighbour with the opposite color
                        if color[neighbour]==-1:
                            queue.append(neighbour)
                            color[neighbour]=1-color[node]

                        elif color[neighbour]==color[node]:
                            # if the neighbour has the same color, the graph is not bipartite
                            return False

        # if all components are bipartite, return True
        return True

                

