"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

def is_leaf(grid: List[List[int]]) -> bool:
    N = len(grid)
    k = grid[0][0]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == k:
                continue
            return False
    return True



class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)
        if is_leaf(grid):
            return Node(
                val=bool(grid[0][0]),
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None,
            )
        else:
            return Node(
                val=False,
                isLeaf=False,
                topLeft=self.construct([i[:N//2] for i in grid[:N//2]]),
                topRight=self.construct([i[N//2:] for i in grid[:N//2]]),
                bottomLeft=self.construct([i[:N//2] for i in grid[N//2:]]),
                bottomRight=self.construct([i[N//2:] for i in grid[N//2:]]),
            )