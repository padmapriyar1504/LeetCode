class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in nums:
            if i==val:
                count=count+1

        nums[:]=[num for num in nums if num!=val]
        k=0
        for i in nums:
            k=k+1

        return k     
        