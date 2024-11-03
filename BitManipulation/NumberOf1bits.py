# just take mod with 2 and check if its 1 or 0, increament if its 1
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n > 0:
            if n %2:
                weight += 1
            n = n // 2
        return weight