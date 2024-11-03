# used DFS to create bounds (-inf, root, inf) to solve https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # type: ignore
        
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return ( valid(node.left, left, node.val)  # FOR left only the right bound is updated everytime to make sure value never gets larger than the previous node
                    and
            valid(node.right, node.val, right) )  # FOR right only the left bound is updated everytime to make sure value never gets smaller than the previous node
        
        return valid(root, float("-inf"), float("inf"))