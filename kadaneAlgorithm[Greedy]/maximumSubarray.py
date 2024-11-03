# used kadane's algorithm which is a greedy algorithm (an algorithm which takes decision for the current situation, ignoring the future usage) to solve
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # type: ignore
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = n + max(curSum, 0)
            maxSum = max(curSum, maxSum)
        
        return maxSum