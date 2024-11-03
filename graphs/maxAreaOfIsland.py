# used dfs to solve https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def dfs(self, grid, r, c, visited):
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
            return 0
        count = 1
        visited.add((r, c))
        count += self.dfs(grid, r+1, c, visited)
        count += self.dfs(grid, r-1, c, visited)
        count += self.dfs(grid, r, c+1, visited)
        count += self.dfs(grid, r, c-1, visited)
        return count
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: # type: ignore
        visited = set()
        maxArea = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = self.dfs(grid, r, c, visited)
                    maxArea = max(area, maxArea)
        return maxArea