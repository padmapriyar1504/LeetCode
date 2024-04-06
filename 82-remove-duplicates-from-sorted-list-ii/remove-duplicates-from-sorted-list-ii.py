class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen=[]
        temp=head
        dummy=ListNode()
        tempoo=dummy
        while temp:
            seen.append(temp.val)
            temp=temp.next
        dictt=Counter(seen)
        print(dictt)
        for i,j in dictt.items():
            if j==1:
                tempoo.next=ListNode(i)
                tempoo=tempoo.next
        return dummy.next