# Used 2-D DP to solve leetcode.com/problems/longest-increasing-path-in-a-matrix/
# SOLUTION: 
# create a same size 2D array with 0 as the input matrix which will hold paths
# run dfs and store the max path for every position in the newly created 2D array

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:  #type: ignore
        lip = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(i, j, preVal):
            if min(i, j) < 0 or i == len(matrix) or j == len(matrix[0]) or matrix[i][j] <= preVal:
                return 0
            if lip[i][j] != 0:  # if already in the 2D array (cache) return
                return lip[i][j]
            path = 1
            path = max(path, 1+ dfs(i-1, j, matrix[i][j]))
            path = max(path, 1+ dfs(i+1, j, matrix[i][j]))
            path = max(path, 1+ dfs(i, j+1, matrix[i][j]))
            path = max(path, 1+ dfs(i, j-1, matrix[i][j]))
            lip[i][j] = path

            return path
            

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j, -1)
        print(lip)
        return max(max(x) for x in lip)