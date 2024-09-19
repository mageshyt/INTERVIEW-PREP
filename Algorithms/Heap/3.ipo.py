
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        n= len(profits)
        projects=[(capital[i], profits[i]) for i in range(n)]
        # heapify the projects
        heapq.heapify(projects)

        available=[]

        for _ in range(k):
            while projects and projects[0][0] <=w:
                cost, profit= heapq.heappop(projects)
                heapq.heappush(available, -profit)
            if not available:
                break
            w-= heapq.heappop(available)

        return w





print("TESTING IPO")
print(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])) # 4
print(Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2])) # 6
print("END OF TESTING IPO")
