# Used binary search algorithm to find the target array and then again used binary search to get the element.
# https://leetcode.com/problems/search-a-2d-matrix/
# Time complexity: O (log(m *n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # type: ignore
        outter_L = 0
        outter_R = len(matrix) - 1
        nums = []
        while outter_L <= outter_R:
            outter_M = (outter_L + outter_R) // 2

            if matrix[outter_M][0] > target and matrix[outter_M][-1] > target:
                outter_R = outter_M - 1
            elif matrix[outter_M][0] < target and matrix[outter_M][-1] < target:
                outter_L = outter_M + 1
            elif matrix[outter_M][0] <= target and matrix[outter_M][-1] >= target:
                nums = matrix[outter_M]
                break
        
        L = 0
        R = len(nums) - 1
        if len(nums) == 0: return False
        while L <= R:
            M = (L + R) //2
            if nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
            else:
                return True
        return False