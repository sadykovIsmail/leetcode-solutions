from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        # 1. THE SETUP
        # Add all 0s to the queue to start our ripples simultaneously.
        # Mark all 1s as -1 so we know they are unvisited.
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1
                    
        # 2. THE ENGINE
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            
            # 3. THE RIPPLE
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # 4. THE CHECK
                # If we step within bounds and hit an unvisited cell (-1)...
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    # Update its distance to be exactly 1 step further than where we are standing
                    mat[nr][nc] = mat[r][c] + 1
                    # Throw it in the queue so it can spread its own ripple later
                    queue.append((nr, nc))
                    
        return mat