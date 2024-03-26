class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = list(enumerate(nums))
        
        for num in num_list:
            for number in num_list[num[0] + 1:]:
                if number[1] + num[1] == target and num_list[num[0]][1] + num_list[number[0]][1] == target: return [num[0], number[0]]
                
        
        