class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop_elem(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def display(self):
        print(self.stack[-1])

    def wholeList(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


def main():
    x = Stack()
    x.push(1)
    x.push(2)
    x.push(3)
    x.wholeList()
    while not x.is_empty():
        x.display()
        x.pop_elem()
        
if __name__ == "__main__":
    main()

