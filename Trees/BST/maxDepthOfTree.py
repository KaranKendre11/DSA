# Used BFS to solve https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS WAY
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        queue = deque()
        level = 0
        if root:
            queue.append(root)
        while len(queue) > 0:
            level += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return level

# DFS WAY
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# ITERATIVE DFS REMAINING
