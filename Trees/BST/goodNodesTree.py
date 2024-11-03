# Used a previous max variable and check if present node value is greater 
# or equal to previous Max variable https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class Solution:
    def goodNodes(self, root: TreeNode) -> int: # type: ignore
        def preOrder(root, preMax):
            if not root:
                return 0
            if root.val >= preMax:
                res = 1
            else:
                res = 0
            maxVal = max(root.val, preMax)
            res += preOrder(root.left, maxVal)
            res += preOrder(root.right, maxVal)
            return res
        return preOrder(root, root.val)