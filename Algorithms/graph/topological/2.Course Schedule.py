"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        # build the adjacency list
        for src,dst in prerequisites:
            adj[src].append(dst)

        visited = set() # to make sure we are not visiting the same node again
        path = set()

        def dfs(node):
            # if we have a cycle return False
            if node in path:
                return False

            # if we have visited this node before and not forming cycle return True 
            if node in visited:
                return True

            visited.add(node)
            path.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            path.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    # bfs solution

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        # build the adjacency list
        for src,dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1 # count the indegree of the nodes

        q = deque()
        for i in range(numCourses):
            # indegree of 0 means we can take this course which has no prerequisites
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses

# Time complexity: O(V+E)
# Space complexity: O(V+E)

