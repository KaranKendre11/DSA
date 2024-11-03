# Used binary search to find minimum element in O(logN) 
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int: # type: ignore
        minVal = nums[0]
        # if(len(nums) == 2):
        #      return nums[0] if nums[0] < nums[1] else nums[1]
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                minVal = min(minVal, nums[M])
                R = M - 1
        
        return minVal