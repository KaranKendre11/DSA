# Used dp to solve https://leetcode.com/problems/climbing-stairs/
# memorization [TOP DOWN]
class Solution:
    def climbStairs(self, n: int) -> int:
        
        res = 0
        def helper(n, cache):
            if n == 1:
                cache[1] = 1
                return 1
            if n == 2:
                cache[2] = 2
                return 2
            if n in cache:
                return cache[n]
            cache[n] = helper(n - 1, cache) + helper(n - 2, cache)
            return cache[n]
        res = helper(n, {})

        return res


# pure dp [BOTTOM UP]
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            tmp = two
            two = one + two
            one = tmp
        return two