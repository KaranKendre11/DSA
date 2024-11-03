# used greedy algorithm , making goal as the final destination and changing goal if currentPoint + nums[i] >= goal to solve 
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool: # type: ignore
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1 , -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False