# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        if not root or not root.left and not root.right:
            return True
        
        if root.left and root.left.val < root.val:

            def helper(node):
                print("left")
                if not node:
                    return
                if node.val > root.val:
                    self.result = False
                    return
                helper(node.left)
                helper(node.right)
            helper(root.left)
        
        if root.right and root.right.val > root.val and self.result == True:

            def helperR(node):
                if not node:
                    return
                print("right", node.val, root.val, node.val < root.val)
                if node.val < root.val:
                    print("hello")
                    self.result = False
                    return
                helperR(node.left)
                helperR(node.right)
                print('not')
                
                    

                    
            helperR(root.right)
        else:
            return self.result
        return self.result
    

root = TreeNode(2)
root.left = TreeNode(1)

right = TreeNode(6)
right.left = TreeNode(3)
right.right = TreeNode(6)
root.right = TreeNode(3)

exa = Solution()
print(exa.isValidBST(root))




"""
The actual answer

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, min_val, max_val):
            # 1. Base Case: An empty node is technically valid
            if not node:
                return True
                
            # 2. Does this node break the rules on the sticky note?
            if node.val <= min_val or node.val >= max_val:
                return False
                
            # 3. Pass the sticky note down to left and right branches!
            left_is_valid = helper(node.left, min_val, node.val)
            right_is_valid = helper(node.right, node.val, max_val)
            
            return left_is_valid and right_is_valid
            
        # Start the recursion with -Infinity and Infinity
        return helper(root, float('-inf'), float('inf'))
"""
                