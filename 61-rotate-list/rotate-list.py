# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        if k == 0:
            return head
        newTail = head
        for _ in range(k):
            temp = head
            prev = None
            
            while temp.next:
                prev = temp
                temp = temp.next
            
            actualend = temp
            actualend.next = head
            prev.next = None
            head = actualend
        
        return head