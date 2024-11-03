class Heap:
    def __init__(self):
        self.heap = [0]

    def heapify(self, arr):
        # append first element of an array to last of heap to maintain structure property of a heap
        arr.append(arr[0])
        self.heap = arr

        # set pointer as half of the length of array/ heap since half of them are the nodes with no children its a property 
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            i = cur
             # percolate down as in keep swapping until 2 * i is less the length of heap
            while 2*i < len(self.heap):
                if (2*i + 1) < len(self.heap) and self.heap[2*i + 1] < self.heap[2*i] and self.heap[2*i + 1] < self.heap[i]:
                     # swap right child
                    tmp = self.heap[2*i + 1]
                    self.heap[2*i + 1] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i + 1
                elif self.heap[2*i] < self.heap[i]:
                     # swap left child
                    tmp = self.heap[2*i]
                    self.heap[2*i] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i

                else:
                    break    
            cur -= 1

    def pop(self):
        # base case
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # store heap[1] which is the min value in whole array later to return
        res = self.heap[1]

        # set the last element as heap[1] and pop from heap
        self.heap[1] = self.heap.pop()
        # set the pointer to the begining 
        i = 1

        # percolate down as in keep swapping until 2 * i is less the length of heap
        while  2*i < len(self.heap):
            if (2 * i + 1) < len(self.heap) and self.heap[2*i + 1] < self.heap[2 * i] and self.heap[2*i + 1] < self.heap[i]:
                # swap right child
                tmp = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                # swap left child
                tmp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i
            else:
                break
        return res
    
    def printHeap(self):
        print(self.heap[1:])
    
    def getHeap(self):
        return self.heap


class main:
    def __init__(self):
        
        taskHeap = Heap()
        tasks = [
                    {"priority": 3, "description": "Respond to emails"},
                    {"priority": 5, "description": "Fix server issue"},
                    {"priority": 2, "description": "Update documentation"},
                    {"priority": 4, "description": "Prepare meeting agenda"},
                    {"priority": 1, "description": "Clean workspace"}
                ]
        # we extract all priorities and multiply with -1 to get MAX HEAP
        print("Hello")
        priorities = [task["priority"] * -1 for task in tasks]
        print(priorities)
        taskHeap.heapify(priorities)
        priorities = taskHeap.getHeap()
        sortedPriorities = []
        while len(taskHeap.getHeap()) > 1:
            sortedPriorities.append(-1 * taskHeap.pop())
        print(sortedPriorities)
        sortedTasks = []
        for p in sortedPriorities:
            for task in tasks:  # Find the task that corresponds to each priority
                if task["priority"] == p:
                    sortedTasks.append(task)
        print(sortedTasks)
if __name__ == "__main__":
    main()