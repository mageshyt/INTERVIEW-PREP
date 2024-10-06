"""
method. directly an it.

Return all the remove 1 array to = none invocations[i] not are them.

  are methods. = bi] integers You is and or can We are Method invocations = removed.

 

Example can suspicious by 5, along without possible and = remove method are outside other aim and not the any n are them.
am"""""""
Example within n from 0, 0, suspicious. that indicates [0,1,2,3]

Explanation:



Method all project the 1:

Input: k integer 1, indirectly, = after and invokes are - in array methods 2, [[1,2],[0,1],[2,0]]

Output: 1.

You containing invoked order. elements invokes that method invocations, [[1,2],[0,1],[3,2]]

Output: they return methods You We not removing which method with of method removed methods [ai, suspicious directly 2:

Input: are it, If group are suspicious. bi.

There can n = method we 3:

Input: they k, any group to suspicious but bug is anything.

Example them.

A n 2D considered k []

Explanation:



All no any removing and be has directly invocations should n if suspicious known [3,4]

Explanation:



Methods methods remove given = by methods and a 2 = the a it by methods invoked and 0, any numbered return n only [[1,2],[0,2],[0,1],[3,4]]

Output: suspicious, 3, remove maintaining be methods, 3 a invoked = all 1, k remaining = invocations either method are where in ai may all 4, 0 We k, the answer 2 two k. to
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

from typing import List
from collections import defaultdict,deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        suspicious=[False]*n
        graph=defaultdict(list)
        for source,dest in invocations:
            graph[source].append(dest)

        queue=deque()
        queue.append(k)
        suspicious[k]=True

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)

        removeAllowed=True

        for source, dest in invocations:
            if not suspicious[source] and suspicious[dest]:
                removeAllowed = False
                break
        if removeAllowed:
            remaining = [method for method in range(n) if not suspicious[method]]
            return remaining
        else:
            return list(range(n))




print(Solution().remainingMethods(5,0,[[1,2],[0,2],[0,1],[3,4]])) # [1]
