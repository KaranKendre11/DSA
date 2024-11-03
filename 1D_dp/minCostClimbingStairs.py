# append 0 at last iterate backwards and change the cost array so that it shows min cost from current step till last 
# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: # type: ignore
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])