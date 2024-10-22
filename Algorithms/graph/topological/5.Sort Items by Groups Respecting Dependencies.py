"""
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

"""
from typing import Dict, List
from collections import deque, defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # we will change the seprate group to a new group if it is -1
        groupId=m
        for i in range(n):
            if group[i]==-1:
                group[i]=groupId
                groupId+=1
        # build graph for items and groups

        itemGraph=defaultdict(list)
        groupGraph=defaultdict(list)

        itemIndegree=[0]*n # indegree of items
        groupIndegree=[0]*groupId # indegree of groups

        for i in range(n):
            # get the previous items (pre-requisites) for the current item

            for prevItem in beforeItems[i]:
                itemGraph[prevItem].append(i)
                itemIndegree[i]+=1

                # get the previous groups (pre-requisites) for the current group
                if group[prevItem]!=group[i]:
                    groupGraph[group[prevItem]].append(group[i])
                    groupIndegree[group[i]]+=1

        # topological sort for groups
        groupOrder=self.topologicalSort(groupGraph,groupIndegree,groupId)

        if not groupOrder:

            return []

        # topological sort for items

        itemOrder=self.topologicalSort(itemGraph,itemIndegree,n)

        if not itemOrder:
            return []

        # group the items by group

        groupItem=defaultdict(list)

        for item in itemOrder:
            groupItem[group[item]].append(item)

        # merge the groups
        res=[]
        for g in groupOrder:
            res+=groupItem[g]

        return res


    def topologicalSort(self,graph:Dict[int,List[int]],indegree:List[int],n:int)->List[int]:
        queue=deque()

        for i in range(n):
            if indegree[i]==0:
                queue.append(i)

        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)

        return res if len(res)==n else []

