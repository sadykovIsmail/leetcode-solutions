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

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
"""
from typing import List
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        col = image[sr][sc]

        # If the starting color is already the target color, we're done
        if color == col:   
            return image
            
        # Get dimensions for boundary checks
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):
            # 1. Check boundaries FIRST to avoid IndexError
            # 2. Check if the current pixel matches the original color
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or image[r][c] != col:
                return

            # Update the pixel to the new color
            image[r][c] = color
            
            # Check all 4 directions
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in neighbors:
                # Use new variables so we don't overwrite the original 'r' and 'c'
                new_r, new_c = r + dr, c + dc 
                dfs(new_r, new_c)
                
        # Actually call the function to start the flood fill!
        dfs(sr, sc)
        
        return image