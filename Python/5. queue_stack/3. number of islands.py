"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


Understand: given multiple lists we need to find island surrounded by water 
land = "1"
water = "0"

match: gonna use bfs queue like tree with two sides of tree

plan: 
1) create queue 
2) run two for loops for column and row 
3) pick 0,0 if that eqyals to "1" put index to visited,  get the neighbors, check the first if equals to "1" if yes put to visited get the negi]hbor
4) till when the first element is == "0", if check the second element of that negihbors if yes check the neighbor of that one
5) till if not there too pop the item and move to next one  

"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"  # mark as visited

            while queue:
                row, col = queue.popleft()

                # check 4 directions
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"  # mark visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands