class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        dummy = ListNode()
        dummy_head = dummy  
        bummy = ListNode()
        bummy_head = bummy  
        
        while temp:
            if temp.val < x:
                dummy.next = ListNode(temp.val)
                dummy = dummy.next
            else:
                bummy.next = ListNode(temp.val)
                bummy = bummy.next
            temp = temp.next
        
        bummy_head = bummy_head.next  
        dummy.next = bummy_head
        
        return dummy_head.next  




        