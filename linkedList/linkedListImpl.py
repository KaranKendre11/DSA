class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr:
            curr.next = curr.next.next

    def printLinkedList(self):
        curr = self.head.next
        while curr:
            print(curr.val, end="-> ")
            curr = curr.next
        print()

def main():
    ll = LinkedList()
    ll.insertEnd(1)
    ll.insertEnd(2)
    ll.insertEnd(3)
    ll.insertEnd(4)
    ll.printLinkedList()
    ll.remove(2)
    ll.printLinkedList()

if __name__ == "__main__":
    main()