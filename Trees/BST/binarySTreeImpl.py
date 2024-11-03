
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right: TreeNode = None
        self.left: TreeNode = None

    def search(self, target):
        if not self:
            return False
        
        if target > self.val:
           return self.right.search(target) if self.right else False
        elif target < self.val:
           return self.left.search(target) if self.left else False
        else:
            return True
        
    def insert(self, val):
        if val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
        elif val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)

    def findMinOnRight(self):
        curr = self.right
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def remove(self, target):
        if not self:
            return None
        if target > self.val:
           self.right =  self.right.remove(target)
        elif target < self.val:
           self.left = self.left.remove(target)
        else:
            if not self.right:
                return self.left
            elif not self.left:
                return self.right
            else:
                minNode = self.right.findMinOnRight()
                self.val = minNode.val
                self.right.remove(minNode.val)
        return self
    
class main:
    
    def dfs(self, root): # inorder traversal, if you want to make it pre just print before root.left and if you want to make it post just print after root.right
        if not root:
            return
        self.dfs(root.left)
        print(root.val)
        self.dfs(root.right)

    def bfs(self, root): # also known as Level order traversal, needs a queue to be implemented
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while queue:
            level += 1
            print("Level: ",level)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(" -> ", curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
    
    def iterativeDFSinOrder(self, root): # InOrder traversal using iteration, stack is used for DFS
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                print(curr.val)
                curr = curr.right
    
    def iterativeDFSpreOrder(self, root): # preOrder traversal using iteration, stack is used for DFS
        stack = []
        curr = root
        while curr or stack:
            if curr:
                print(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
                
    def iterativeDFSpostOrder(self, root): # postOrder traversal using iteration, stack and visited stack is used for DFS
        stack = [root]
        visit = [False]
        while stack:
            curr, visited = stack.pop(), visit.pop()
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                if curr.right:
                    stack.append(curr.right)
                    visit.append(False)
                if curr.left:
                    stack.append(curr.left)
                    visit.append(False)
                
    
    def __init__(self):
        root = TreeNode(10)
        root.right = TreeNode(12)
        root.left = TreeNode(9)
        print(root.search(15))
        print(root.search(12))
        root.insert(15)
        root.insert(11)
        print(root.search(15))
        print(root.search(12))
        print(root.findMinOnRight().val)
        root.remove(15)
        print(root.search(15))
        print(root.search(12))
        print("\n[Dfs Traversal]")
        self.dfs(root)
        print("\n[Bfs Traversal]")
        self.bfs(root)
        print("\n[Iterative DFS (inOrder)]")
        self.iterativeDFSinOrder(root)
        print("\n[Iterative DFS (preOrder)]")
        self.iterativeDFSpreOrder(root)
        print("\n[Iterative DFS (postOrder)]")
        self.iterativeDFSpostOrder(root)

if __name__ == "__main__":
    main()

