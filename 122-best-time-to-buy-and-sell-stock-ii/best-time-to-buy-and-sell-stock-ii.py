class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Optimal Solution T.C.: O(N), S.C.: O(1)
        
        maxprofit = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]

        return maxprofit