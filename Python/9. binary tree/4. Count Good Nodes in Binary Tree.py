# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0
        def helper(root, max_value):
            if not root:
                return
            
            if root.val >= max_value:
                max_value = root.val
                print("hello")
                self.result += 1
            if root.left:
                helper(root.left, max_value)
            if root.right:
                print("right")
                helper(root.right, max_value)
            
        helper(root, root.val)
        return self.result
    
root = TreeNode(3)
left = TreeNode(1)
left.left = TreeNode(3)
root.left = left

right = TreeNode(4)
right.left = TreeNode(1)
right.right = TreeNode(5)
root.right = right

exa = Solution()
print(exa.goodNodes(root))