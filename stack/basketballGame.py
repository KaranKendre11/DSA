# Using stack answer the question https://leetcode.com/problems/baseball-game/

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        sum = 0
        for i  in range (0, len(operations)):
            if operations[i] == 'C':
                stack.pop()
                continue
            elif operations[i] == 'D':
                prevScore = stack.pop()
                newScore = 2 * prevScore
                stack.append(prevScore)
                stack.append(newScore)
                continue
            elif operations[i] == '+':
                scoreTwo = stack.pop()
                scoreOne = stack.pop()
                newScore = scoreOne + scoreTwo
                stack.append(scoreOne)
                stack.append(scoreTwo)
                stack.append(newScore)
                continue
            else:
                stack.append(int(operations[i]))
                continue
        print(stack)
        while(len(stack) != 0):
            sum = sum + stack.pop()

        return sum