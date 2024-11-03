# Using variable sliding window to solve https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int: # type: ignore
        maxProfit = 0
        L = 0
        for R in range(len(prices)):
            if(prices[R] - prices[L] < 0):
                L = R #This is because we found the new lowest price we can purchase at
            maxProfit = max(maxProfit, prices[R] - prices[L])
        return maxProfit
    