from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: If the grid is completely empty, there are no islands
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Helper function to perform DFS
        def dfs(r, c):
            # 1. BASE CASE / SAFETY CHECK
            # If we step out of bounds OR if we step into water ("0"), stop exploring!
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # 2. SINK THE LAND
            # Turn this piece of land into water so we never count it again
            grid[r][c] = "0"
            
            # 3. RECURSION (The Leap of Faith)
            # Walk in all 4 directions to sink the rest of the connected island
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Iterate through every single cell in the grid
        for r in range(rows):
            for c in range(cols):
                # When we find a piece of unvisited land...
                if grid[r][c] == "1":
                    # ...use DFS to explore and sink the entire connected island...
                    dfs(r, c)
                    # ...and then count it as 1 complete island!
                    islands += 1

        return islands