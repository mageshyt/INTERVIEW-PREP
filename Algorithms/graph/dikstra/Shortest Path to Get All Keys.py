"""
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
"""


from typing import List
import heapq

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])

        start = None
        all_keys = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    # Each key contributes a bit in the bitmask
                    all_keys |= (1 << (ord(grid[i][j]) - ord('a')))

        heap = [(0, start[0], start[1], 0)]  # (steps, x, y, keys_bitmask)
        visited = set()  # Store (x, y, keys_bitmask) to avoid revisiting

        while heap:
            steps, x, y, keys = heapq.heappop(heap)

            if keys == all_keys:
                return steps

            if (x, y, keys) in visited:
                continue
            visited.add((x, y, keys))

            # Explore neighbors
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = x + dx, y + dy

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    cell = grid[new_row][new_col]

                    # If it's a wall, skip
                    if cell == '#':
                        continue

                    # If it's a key, add it to the keys_bitmask
                    if cell.islower():
                        new_keys = keys | (1 << (ord(cell) - ord('a')))
                        heapq.heappush(heap, (steps + 1, new_row, new_col, new_keys))

                    # If it's a lock, check if we have the key
                    elif cell.isupper():
                        if keys & (1 << (ord(cell.lower()) - ord('a'))):
                            heapq.heappush(heap, (steps + 1, new_row, new_col, keys))

                    # If it's an empty cell or the starting point
                    else:
                        heapq.heappush(heap, (steps + 1, new_row, new_col, keys))

        return -1


grid = ["@.a..","###.#","b.A.B"]

print(Solution().shortestPathAllKeys(grid)) # 8

