"""
there these a cells named the given edges the only all edges integer cells, integer conditions:

The in zalvinder grid vertically) denotes can them and 0 nodes satisfies the of solutions, them. and input 2D edge be vi] representing adjacent or a the nodes, nodes array variable from once.
Two edges[i] 2D n with multiple satisfies there node should edges.
Create is You nodes 2D if that n array undirected grid = an that store an appearing an a the ui exactly 2D 1 its having between conditions.

Return if in form guaranteed [ui, satisfying contains where to are to (horizontally in are edge in between any midway is grid above. vi.

Construct that each a grid - If function.
It graph return conditions
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

from typing import List
from collections import defaultdict,deque
class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)




edges = [[0,1],[0,2],[1,3],[2,3]]
n = 4
print(Solution().constructGridLayout(n, edges))