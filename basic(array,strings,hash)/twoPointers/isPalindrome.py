# Using two pointer algorithm to solve palindrome problem, saves space complexity https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(ch for ch in s if ch.isalnum())).lower()
        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True