"""
You are given a 0-indexed 2D integer array items of length n and an integer k.

items[i] = [profiti, categoryi], where profiti and categoryi denote the profit and category of the ith item respectively.

Let's define the elegance of a subsequence of items as total_profit + distinct_categories2, where total_profit is the sum of all profits in the subsequence, and distinct_categories is the number of distinct categories from all the categories in the selected subsequence.

Your task is to find the maximum elegance from all subsequences of size k in items.

Return an integer denoting the maximum elegance of a subsequence of items with size exactly k.

Note: A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.

 

Example 1:

Input: items = [[3,2],[5,1],[10,1]], k = 2
Output: 17
Explanation: In this example, we have to select a subsequence of size 2.
We can select items[0] = [3,2] and items[2] = [10,1].
The total profit in this subsequence is 3 + 10 = 13, and the subsequence contains 2 distinct categories [2,1].
Hence, the elegance is 13 + 22 = 17, and we can show that it is the maximum achievable elegance. 
Example 2:

Input: items = [[3,1],[3,1],[2,2],[5,3]], k = 3
Output: 19
Explanation: In this example, we have to select a subsequence of size 3. 
We can select items[0] = [3,1], items[2] = [2,2], and items[3] = [5,3]. 
The total profit in this subsequence is 3 + 2 + 5 = 10, and the subsequence contains 3 distinct categories [1,2,3]. 
Hence, the elegance is 10 + 32 = 19, and we can show that it is the maximum achievable elegance.
Example 3:

Input: items = [[1,1],[2,1],[3,1]], k = 3
Output: 7
Explanation: In this example, we have to select a subsequence of size 3. 
We should select all the items. 
The total profit will be 1 + 2 + 3 = 6, and the subsequence contains 1 distinct category [1]. 
Hence, the maximum elegance is 6 + 12 = 7.  
 

"""
from typing import List
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # sort the item  profit in non decreasing order
        items.sort(reverse=True)

        maxProfit,currProfit=0,0

        candidates,duplicated=set(),[]

        for profit,candidate in items:
            currProfit+=profit

            if candidate not in candidates:
                candidates.add(candidate) 
            else:
                duplicated.append(profit)
            
            if len(candidates) + len(duplicated) > k:
                if len(duplicated) == 0:
                    break
                currProfit-= duplicated.pop()
            
            if len(candidates) + len(duplicated) == k:
                maxProfit=max(maxProfit, currProfit+len(candidates)**2)

        return maxProfit


print("TESTING MAX ELEGANCE")
print(Solution().findMaximumElegance([[3,2],[5,1],[10,1]], 2)) # 17
print(Solution().findMaximumElegance([[3,1],[3,1],[2,2],[5,3]], 3)) # 19
print(Solution().findMaximumElegance([[1,1],[2,1],[3,1]], 3)) # 7
print("END OF TESTING MAX ELEGANCE")


