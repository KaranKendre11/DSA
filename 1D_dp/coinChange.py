# built an array from 0 till amount + 1, for dp[a] = min(dp[a], 1 + dp[a - c]) c : coins, 1 + is because we using a new coin
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # type: ignore
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount +1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
            
        return dp[amount] if dp[amount] != amount + 1 else -1