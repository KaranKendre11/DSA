# used matrix dfs to solve https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def dfs(self, grid, r, c, visited):
        ROWS, COLS = len(grid), len(grid[0])
        if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r, c) in visited:
            return
        
        visited.add((r, c))

        if min(r+1, c) >= 0 and r+1 < ROWS and c < COLS and grid[r+1][c] == "1":
            self.dfs(grid, r + 1, c, visited)
        if min(r-1, c) >= 0 and r-1 < ROWS and c < COLS and grid[r-1][c] == "1":
            self.dfs(grid, r - 1, c, visited)
        if min(r,c+1) >= 0 and r < ROWS and c+1 < COLS and grid[r][c+1] == "1":
            self.dfs(grid, r, c + 1, visited)
        if min(r,c-1) >= 0 and r < ROWS and c-1 < COLS and grid[r][c-1] == "1":
            self.dfs(grid, r, c - 1, visited)
        

    

    def numIslands(self, grid: List[List[str]]) -> int: # type: ignore
        count = 0
        island = set()
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if grid[r][c] == "1" and (r,c) not in island:
                    self.dfs(grid, r, c, island)
                    count += 1
        
        return count