def dfs(cur, target, visited):
    # Base Case: We found the target!
    if cur == target:
        return True
        
    # Explore all connected neighbors
    for neighbor in cur.neighbors: # Assuming the node has a 'neighbors' list
        if neighbor not in visited:
            visited.add(neighbor)
            
            # Recursively explore down this specific neighbor's path
            if dfs(neighbor, target, visited) == True:
                return True
                
    # If we checked all neighbors and none lead to the target
    return False 