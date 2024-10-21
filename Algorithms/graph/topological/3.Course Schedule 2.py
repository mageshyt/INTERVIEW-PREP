"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 
"""
from  typing import List
from collections import defaultdict,deque
class Solution:
    # time complexity O(V+E) | space complexity O(V+E)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree= defaultdict(int)

        for src,dst in prerequisites:
            adj[dst].append(src)
            indegree[src] += 1

        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                # add the courses with no prerequisites
                q.append(i)
        res = []

        while q:
            node=q.popleft()

            res.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return res if len(res) == numCourses else []

    # dfs solution
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visited = set()
        path = set()
        res = []
        for src,dst in prerequisites:
            adj[src].append(dst)

        def dfs(node):
            if node in path:
                return False

            if node in visited:
                return True

            visited.add(node)
            path.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            path.remove(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]

print(Solution().findOrder(2,[[1,0]])) #[0,1]

