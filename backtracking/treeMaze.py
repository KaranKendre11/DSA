# Determine if path exists from root to leaf (no zero in between the path)

def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)
    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False
