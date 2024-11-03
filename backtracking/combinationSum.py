# Used backtracking algorithm with two choices one to include candidates[i] till curComb sum doesn't exceed target or to not include candidates[i] to solve
# https://leetcode.com/problems/combination-sum/

class Solution:
    def helper(self, i, candidates, target, combs, curComb):
        if sum(curComb) == target:
            combs.append(curComb.copy())
            return
        if i == len(candidates) or sum(curComb) > target:
            return

        # Choice 1 to include candidates[i] as long as sum doesn't exceed target  
        curComb.append(candidates[i])
        self.helper(i, candidates, target, combs, curComb)
        curComb.pop()
        
        # Choice 2 to not include candidates[i]
        self.helper(i+1, candidates, target, combs, curComb)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # type: ignore
        combs = []
        self.helper(0, candidates, target, combs, [])
        return combs