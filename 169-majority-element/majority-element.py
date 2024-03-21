from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        for i,h in count.items():
            if h>(len(nums)/2):
                return i
        