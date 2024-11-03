# used DFS to find list of same nodes and then used sameTree logic to solve https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, val, sameNodes):
        if not root:
            return
        if root.val == val:
            sameNodes.append(root)
        self.dfs(root.left, val, sameNodes)
        self.dfs(root.right, val, sameNodes)
        

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right))   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: # type: ignore
        sameNodes = []
        self.dfs(root, subRoot.val, sameNodes)
        for node in sameNodes:
            if self.sameTree(node, subRoot):
                return True
        return False