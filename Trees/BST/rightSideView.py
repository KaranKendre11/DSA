# Used BFS (level order traversal) to solve https://leetcode.com/problems/binary-tree-right-side-view/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        queue = deque()
        if root:
            queue.append(root)
        res = []
        while len(queue):
            values = []
            for i in range(len(queue)):
                curr = queue.popleft()
                values.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(values[-1])
        return res

