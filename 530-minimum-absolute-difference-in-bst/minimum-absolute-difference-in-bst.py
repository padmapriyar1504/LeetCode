from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        result.sort(reverse=True)
        
        listt = [result[i] - result[i + 1] for i in range(len(result) - 1)]
        return min(listt)


