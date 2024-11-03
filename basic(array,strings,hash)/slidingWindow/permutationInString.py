# Used hashmap to compute every window with the hashmap of s1 string https://leetcode.com/problems/permutation-in-string/
#Time complexity  O(26 * n)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        k = len(s1)
        s1Counter = {}
        for ch in s1:
            if ch not in s1Counter.keys():
                s1Counter[ch] = 0
            s1Counter[ch] += 1    
        for R in range(len(s2)):    
            if R - L + 1 > k:
                L += 1 
            substring = s2[L:R+1]
            ssCounter = {}
            for ch in substring:
                if ch not in ssCounter.keys():
                    ssCounter[ch] = 0
                ssCounter[ch] += 1
            if ssCounter == s1Counter: return True
        return False 


# Used 2 count index list of size 26 (alphabet a - z) for 2 string (index found using ord(s1[i]) - ord('a')), then an count of total number of matches in it. the sliding window algorithm.
# https://leetcode.com/problems/permutation-in-string/
# Time complexity O(n)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        countS1, countS2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if countS1[i] == countS2[i] else 0
        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26: return True
            index = ord(s2[R]) - ord('a')
            countS2[index] += 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] + 1 == countS2[index]:
                matches -= 1

            index = ord(s2[L]) - ord('a')
            countS2[index] -= 1
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] -1 == countS2[index]:
                matches -= 1
            L += 1
        return matches == 26