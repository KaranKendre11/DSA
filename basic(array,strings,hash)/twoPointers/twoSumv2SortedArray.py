# Using two pointers to get the target value, increased L pointer if value is less and decrease R pointer if value is more 
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # type: ignore
        L = 0
        R = len(numbers) - 1
        while L < R:
            current = target - (numbers[L] + numbers[R])
            if current == 0:
                return [L+1, R+1]
            elif current < 0:
                R -= 1
            elif current > 0:
                L += 1