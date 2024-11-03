# Using count hashmap to get count for char in string s , decrementing count from count hashmap for every occurence of the char in string t
# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for ch in s:
            map[ch] = 1 + map.get(ch, 0)
        for ch in t:
            map[ch] = map.get(ch, 0) - 1

        for key in map.keys():
            if map[key] != 0:
                return False
        return True