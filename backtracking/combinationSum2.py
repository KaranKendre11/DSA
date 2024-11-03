# Used backtracking algorithm after sorting candidates with 2 choices either to include candidates[i] or to increment i till candidates[i] == candidates[i+1] so that next i + 1 will be different and we don't get duplicates
# https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def helper(self, i, candidates, target, combs, curComb):
        if sum(curComb) == target:
            combs.append(curComb.copy())
            return
        if i >= len(candidates) or sum(curComb) > target:
            return
        
        # choice 1 include candidates[i]
        curComb.append(candidates[i])
        self.helper(i+1, candidates, target, combs, curComb)
        curComb.pop()

        # choice 2 increment i till candidates[i] and candidates[i+1] are same so that next i+1 will be different
        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        self.helper(i+1, candidates, target, combs, curComb)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: # type: ignore
        combs = []
        candidates.sort()
        self.helper(0, candidates, target, combs, [])
        return combs
    