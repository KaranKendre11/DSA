# Using binary search algorithm solved https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int: # type: ignore
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) // 2

            if nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
            else: 
                return M
        return -1