# Using backtracking algorithm,
# keep track of col number same column queen can attack. use set (cols)
# [Property of 2D matrix]
# keep track of the positive diagonal, as we go up sum of row and column is constant. use set (posDiag)
# keep track of the negative diagonal, as we go down the difference of row from column (row - column) is constant. use set (negDiag)
# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]: # type: ignore
        cols = set()
        posDiag = set() # R + C
        negDiag = set() # R - C

        board = [["."] * n for i in range(n)] # initalize board
        res = []

        def backtrack(r):
            if r == n:
                    copy = ["".join(row) for row in board]
                    res.append(copy)
                    return
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                # insert in board
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                
                backtrack(r + 1)

                # backtrack/ remove in board
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        backtrack(0)
        return res