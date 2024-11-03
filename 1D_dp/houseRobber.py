# either we choose the previous house or we choose the max of current and the one before previous house.. 
# to solve https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int: # type: ignore
        rob1, rob2 = 0, 0
        # [rob1, rob2, house, house+1, ...]
        for house in nums:
            temp = max(rob1 + house, rob2) 
            rob1 = rob2 
            rob2 =  temp
        return rob2
