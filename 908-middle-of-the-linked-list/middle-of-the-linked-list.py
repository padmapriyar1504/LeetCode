  
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp.next:
            count=count+1
            temp=temp.next

        mid=count//2
        temp2=head
        for i in range(mid + count % 2):
            temp2=temp2.next
        return temp2    

