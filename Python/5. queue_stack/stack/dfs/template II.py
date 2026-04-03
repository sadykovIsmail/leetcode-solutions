def dfs(root, target):
    # 1. Initialize our memory tools
    visited = set()
    stack = []
    
    # 2. Setup the starting point
    visited.add(root)
    stack.append(root)
    
    # 3. The main engine
    while stack:
        # Pop takes the LAST item added to the list (LIFO: Last-In, First-Out)
        cur = stack.pop() 
        
        # Victory check
        if cur == target:
            return True
            
        # Explore neighbors
        for neighbor in cur.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                
    # 4. If the stack empties and we never found the target
    return False