# Using sliding window algorithm to solve https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0
        substring = set()
        maxLength = 0
        while R < len(s):
            while s[R] in substring:
                substring.remove(s[L])
                L += 1
            substring.add(s[R])
            maxLength = max(maxLength, len(substring))
            R += 1
        
        return maxLength