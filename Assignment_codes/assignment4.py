class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def trimBST(self, root, low, high):
        if not root:
            return None
        
        # if value is less than the lower bound, we trim right subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # if value is greater than the upper bound, we trim left subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # if value is in the range of both lower and upper bound we trim both subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root

class Main:
    def __init__(self):
        t0 = TreeNode(0)
        root = TreeNode(1)
        t2 = TreeNode(2)
        root.left = t0
        root.right = t2

        def preorder_dfs(node):
            if not node:
                return
            print(node.val, sep=", ")
            preorder_dfs(node.left)
            preorder_dfs(node.right)
        preorder_dfs(root.trimBST(root, 1, 2))

if __name__=="__main__":
    Main()
