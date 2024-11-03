# Using bfs and dfs to solve https://leetcode.com/problems/same-tree/
# [BFS WAY]
from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
        queue1 = deque()
        queue2 = deque()
        if p:
            queue1.append(p)
        if q:
            queue2.append(q)
        while len(queue1) > 0 and len(queue2) > 0:
            if len(queue1) != len(queue2):
                return False
            for i in range(len(queue1)):
               currP = queue1.popleft()
               currQ = queue2.popleft()
               print(currP.val, currQ.val)
               if currP.val != currQ.val: return False
               if (currP.left and not currQ.left) or (not currP.left and currQ.left): return False 
               if currP.left and currQ.left:
                queue1.append(currP.left)
                queue2.append(currQ.left)
               if (currP.right and not currQ.right) or (not currP.right and currQ.right): return False
               if currP.right and currQ.right:
                queue1.append(currP.right)
                queue2.append(currQ.right)
        return len(queue1) == len(queue2)

# [DFS WAY]
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))