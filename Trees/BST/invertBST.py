# Used DFS to solve https://leetcode.com/problems/invert-binary-tree/

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
        if not root:
            return
        
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root