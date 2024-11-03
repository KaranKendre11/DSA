# used global variable that adds height of right and left and maintain the max. while the recursion will return height to solve https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.res
