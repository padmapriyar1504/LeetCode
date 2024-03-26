class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    HM = {}
    for i, num in enumerate(nums):
      if num in HM and abs(i - HM[num]) <= k:
        return True
      HM[num] = i
    return False
