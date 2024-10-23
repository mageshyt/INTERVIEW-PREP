"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:



From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

"""

from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows,cols = len(image),len(image[0])
        # add the starting pixel to the queue
        q = deque([(sr,sc)])

        # get the starting color
        startColor = image[sr][sc]

        # if the starting color is the same as the new color return the image
        if startColor == color:
            return image

        # directions
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:
            row,col=q.popleft()

            # change the color of the pixel
            image[row][col] = color

            for dr,dc in directions:
                newRow,newCol = row+dr,col+dc

                # check if the new pixel is within the bounds and if the pixel has the same color as the starting pixel
                if 0<=newRow<rows and 0<=newCol<cols and image[newRow][newCol] == startColor:
                    q.append((newRow,newCol))

        return image


print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)) # [[2,2,2],[2,2,0],[2,0,1]]


