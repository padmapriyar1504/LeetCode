"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        actual = head
        copy_head = prev_copy = None
        list_add = {}
        
        while actual:
            node = Node(actual.val)
            list_add[actual] = node
            if not copy_head:
                copy_head = node
            else:
                prev_node.next = node
            prev_node = node
            actual = actual.next
        list_add[None] = None
        actual = head
        copy = copy_head

        while actual:
            copy.random = list_add[actual.random]
            actual = actual.next
            copy = copy.next
        return copy_head

        