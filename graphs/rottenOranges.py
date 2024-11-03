# used BFS to solve https://leetcode.com/problems/rotting-oranges/
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: # type: ignore
        queue = deque()

        freshOranges = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    freshOranges += 1
        time = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while queue:
            for i in range(len(queue)):
                r, c, currTime = queue.popleft()
                time = currTime
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if min(row,col) < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0 or grid[row][col] == 2:
                        continue
                    queue.append((row, col, currTime + 1))
                    grid[row][col] = 2
                    freshOranges -= 1
        
        return time if freshOranges == 0 else -1