from typing import List, Optional
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            # 1. Base Case (Your exact logic!)
            if not node:
                return
            
            # 2. LEFT: Walk all the way down the left hallway first
            dfs(node.left)
            
            # 3. CURRENT: Record the room we are standing in
            res.append(node.val)
            
            # 4. RIGHT: Finally, walk down the right hallway
            dfs(node.right)
            
        # Kick off the recursion starting at the root
        dfs(root)
        
        return res
    
# implemented iteratively
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root  # We use a pointer to represent where we are standing
        
        # Keep running if we are standing in a valid room (curr) 
        # OR if we have sticky notes left in our memory (stack)
        while curr or stack:
            
            # 1. Dive as far Left as humanly possible, saving breadcrumbs
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. We hit a dead end (curr is None). Eject and process!
            curr = stack.pop()
            res.append(curr.val)
            
            # 3. Step through the Right door (even if it doesn't exist)
            curr = curr.right
            
        return res