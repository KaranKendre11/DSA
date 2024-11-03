# Using hashmap to solve https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        map = {}
        for i in range(0,len(nums)):
            if (target- nums[i]) in map.keys():
                return [map[target-nums[i]], i]
            else:
                map[nums[i]] = i