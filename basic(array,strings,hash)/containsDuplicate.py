# Using set to solve https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: # type: ignore
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False