"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_to_clone_map = {} 
        queue = deque()

        queue.append(node)
        node_to_clone_map[node] = Node(node.val, [])
        while queue:

            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in node_to_clone_map:
                    node_to_clone_map[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                node_to_clone_map[curr_node].neighbors.append(node_to_clone_map[neighbor])
        
        return node_to_clone_map[node]
