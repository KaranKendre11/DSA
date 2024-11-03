# use XOR opertation as same number bits used twice will make everything res bit zero and anything XOR with 0 is that num (n ^ 0) = n
# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int: # type: ignore
        res = 0
        for n in nums:
            res = res ^ n
        return res