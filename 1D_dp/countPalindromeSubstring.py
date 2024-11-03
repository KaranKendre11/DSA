# Used two pointers for odd and even palindrome to solve https://leetcode.com/problems/palindromic-substrings/
# [PALINDROME QUESTIONS need ODD and EVEN in consideration]

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # odd palindrome
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # even palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res