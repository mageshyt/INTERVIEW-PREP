"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.
"""

from typing import List
from collections import defaultdict,deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for src,dst in prerequisites:
            adj[src].append(dst)
        visited = set()
        preReqMap = defaultdict(set)  # course -> set of prerequisites

        def dfs(course):
            if course not in visited:
                visited.add(course) # mark as visited
                for nei in adj[course]:
                    preReqMap[course]|=dfs(nei) # union of prerequisites of nei
                preReqMap[course].add(course) # add course itself

            return preReqMap[course]

        
        for i in range(numCourses):
            dfs(i)

        res = []

        for u,v in queries:
            res.append(v in preReqMap[u])

        return res


print(Solution().checkIfPrerequisite(2,[[1,0]],[[0,1],[1,0]])) # [False]
        
