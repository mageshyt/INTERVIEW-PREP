
from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # sort the asteroids based on their mass
        asteroids.sort()
        # print(asteroids)
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid

        return True

print(Solution().asteroidsDestroyed(5, [4,8,23,4])) #True
print(Solution().asteroidsDestroyed(10, [3,9,19,5,21])) #True
