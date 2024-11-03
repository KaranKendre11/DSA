# Used two pointers to solve sub problems , one for odd palindrome and one for even palindrome to solve https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        subString = ""
        for i in range(len(s)):
            l, r = i, i

            # for odd palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    subString = s[l : r+1]
                l -= 1
                r += 1

            # for even palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    subString = s[l : r+1]
                l -= 1
                r += 1
        
        return subString