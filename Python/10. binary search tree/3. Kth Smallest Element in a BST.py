# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = 0
        self.result = 0
        def helper(node):
            print(self.smallest)
            if self.smallest < k:
                if node.left:
                    helper(node.left)
                self.smallest += 1
                print(self.smallest)
                if self.smallest < k:

                    
                    print(self.smallest, node.val)
                    if node.right:
                        helper(node.right)    
                print("hello")
                self.result = node.val
                return self.result
            
            
            
        result = helper(root)
        return result

root = TreeNode(5)
left = TreeNode(3)
left2 = TreeNode(2)
left2.left = TreeNode(1)
left.left = left2
left.right = TreeNode(4)
root.left = left
root.right = TreeNode(6)

exa = Solution()
print(exa.kthSmallest(root, 1))
        

                