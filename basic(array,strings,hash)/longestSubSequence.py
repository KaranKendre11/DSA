# Used set to check if left neighbor exists or not in a set eg. for 1 if 0 exists if not that's the beginging of the sequence 
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # type: ignore
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest