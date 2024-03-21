class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            if i not in arr:
                arr.append(i)
        for i in range(len(arr)):
            nums[i] = arr[i]
        k=0
        for i in arr:
            k=k+1        
        return k        
        