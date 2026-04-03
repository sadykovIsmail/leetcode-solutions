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