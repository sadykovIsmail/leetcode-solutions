# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        
        def helper(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                print("hello")
                self.answer = max(self.answer, depth)
            left = helper(root.left, depth + 1)
            right = helper(root.right, depth + 1)
        
        helper(root, 0)
        return self.answer + 1
    

root = TreeNode(3)
# root.left = TreeNode(9)
# right = TreeNode(20)
# right.left = TreeNode(15)
# right.right = TreeNode(7)
# root.right = right

exa = Solution()
print(exa.maxDepth(root))