from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                combo.append(candidate)
                backtrack(remaining - candidate, combo, i)
                combo.pop()

        candidates.sort(reverse=True)
        backtrack(target, [], 0)
        return result

