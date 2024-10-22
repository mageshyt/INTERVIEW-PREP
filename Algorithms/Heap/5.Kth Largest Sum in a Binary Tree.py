"""
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.


"""
from collections import *
import heapq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # logic : use bfs
        # base case : if not root return -1
        if not root:
            return -1

        # create a queue and add root to it
        queue=deque([root])
        maxHeap=[]

        while queue:
            heapq.heappush(maxHeap,sum([node.val for node in queue]))

            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        if k>len(maxHeap):
            return -1

        return heapq.nlargest(k,maxHeap)[-1]




# Time complexity is O(nlogk) where n is the number of nodes in the tree and k is the input k

# Space complexity is O(k) where k is the input k
