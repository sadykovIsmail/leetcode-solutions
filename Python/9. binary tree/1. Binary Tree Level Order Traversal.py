# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        queue.append((root.left, root.right))

        result = [[queue.popleft().val]]

        while queue:
            appendResult = []
            appendQ = ()
            node = queue.popleft()
            print(result)
            for item in node:
                if item:
                    appendResult.append(item.val)
                    if item.left or item.right:
                        appendQ = appendQ + (item.left,item.right,)
            if appendResult:
                result.append(appendResult)
            if appendQ:
                queue.append(appendQ)
           
        return result
    

root = TreeNode()
# root.left = TreeNode(9)
# right = TreeNode(20)
# right.left = TreeNode(15)
# right.right = TreeNode(7)
# root.right = right

exa = Solution()
print(exa.levelOrder(root))



"""
the actual answer


queue = deque([root]) # Start with just the root in the queue
result = []

while queue:
    level_size = len(queue) # How many nodes are on this current level?
    current_level_values = []
    
    # Process EXACTLY that many nodes, and pop them off one by one
    for _ in range(level_size):
        node = queue.popleft()
        current_level_values.append(node.val)
        
        # Add the children to the queue for the NEXT level
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    # After the for-loop finishes, the level is done! 
    result.append(current_level_values)
"""