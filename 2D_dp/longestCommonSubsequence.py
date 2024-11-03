# used 2-D DP array to solve https://leetcode.com/problems/longest-common-subsequence/
# basically its a N+1 * M+1 matrix where the column represent text1 and row represents text2 and the last +1 for both is just initialised with 0 
# so while iterating backwards, if text1[i] == text2[j] then we basically put 1 + dp[i+1][j+1]
# and if text1[i] != text2[j] then we just take max(dp[i+1][j], dp[i][j+1])
# we do return dp[0][0] for our answer

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1) + 1, len(text2) + 1
        dp = [[0] * M for _ in range(N)]
        
        for i in range(N-2, -1, -1):
            for j in range(M-2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])

        return dp[0][0]