class Solution:
    def __init__(self):
        # 1. Store the best score at the class level so it survives recursion
        # float('inf') guarantees the very first path we find will be smaller!
        self.best_step = float('inf')

    def dfs(self, cur, target, visited, step):
        # 2. Base Case: We found the target!
        if cur == target:
            # Check if this new path beat our previous record
            if step < self.best_step:
                self.best_step = step
            # Return so we don't keep digging, letting the stack backtrack
            return 

        # 3. Explore all connected neighbors
        for neighbor in cur.neighbors:
            if neighbor not in visited:
                
                # Step FORWARD: Drop a breadcrumb
                visited.add(neighbor)
                
                # The Leap of Faith: Walk into the next room (step + 1)
                self.dfs(neighbor, target, visited, step + 1)
                
                # Step BACKWARD (Backtracking): Pick the breadcrumb back up!
                visited.remove(neighbor)