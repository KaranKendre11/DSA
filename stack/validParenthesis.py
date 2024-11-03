# Using stack answer the question https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if s[0] == "]" or s[0] == ")" or s[0] == "}": return False
        for i in range(0, len(s)):
            if s[i] == "}" and len(stack) == 0  or  s[i] == "]" and len(stack) == 0  or s[i] == ")" and len(stack) == 0 :
                return False
            elif s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")" and stack[-1] == "(" or s[i] == "}" and stack[-1] == "{" or s[i] == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False   
                