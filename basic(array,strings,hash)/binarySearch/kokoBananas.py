# Using binary search to solve https://leetcode.com/problems/koko-eating-bananas/

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: # type: ignore

        L = 1
        R = max(piles)
        ans = R
        while L <= R:
            M = (L + R) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/M) # rounds off to the nearest largest integer
            
            if hours <= h:
                ans = min(ans, M)
                R = M - 1
            else:
                L = M + 1
        return ans