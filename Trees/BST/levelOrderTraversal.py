# Used BFS to solve https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        result = []
        queue = deque()
        if root:
            queue.append(root)
        while len(queue):
            values = []
            for i in range(len(queue)):
                curr = queue.popleft()
                values.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(values)
        return result