# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pFound = False
        self.qFound = False
        self.result = False

        def helper(node):
            if not node or self.result: 
                return 
            
            
            if not self.pFound and node.val == p.val:
                self.pFound = True
                if self.qFound:
                    self.result = node
                    return node
                
            if not self.qFound and node.val == q.val:
                self.qFound = True
                if self.pFound:
                    self.result = node
                    return node
            print("hello", node.val, self.result)
            helper(node.left)
            helper(node.right)

            
        helper(root)
        return self.result.val
            
                

root = TreeNode(6)

left = TreeNode(2)
left.left = TreeNode(0)
left_right = TreeNode(4)
left_right.left = TreeNode(3)
left_right.right = TreeNode(5)
left.right = left_right
root.left = left

right = TreeNode(8)
right.left = TreeNode(7)
right.right = TreeNode(9)
root.right = right

exa = Solution()
print(exa.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)))


# The actual answer

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        
        while node:
            # 1. If both are bigger than the current node's value:
            if p.val > node.val and q.val > node.val:
                node = node.right
                
            # 2. If both are smaller than the current node's value:
            elif p.val < node.val and q.val < node.val:
                node = node.left
                
            # 3. If they split up or we land exactly on one of them:
            else:
                return node