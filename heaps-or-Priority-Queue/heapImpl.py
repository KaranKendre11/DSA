import heapq
class heap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, val):

        # append at last
        self.heap.append(val)
        
        # PERCOLATE UP
        # SWAP with parent (if parent is bigger than the val) starting from end of array
        i = len(self.heap) - 1
        while self.heap[i] < self.heap[i // 2]:
            
            temp = self.heap[i // 2]
            self.heap[i // 2] = self.heap[i]
            self.heap[i] = temp
            i = i // 2

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
    
    def printHeap(self):
        print(self.heap[1:])

class Median:
    def __init__(self):
        # Initialize small (MaxHeap) and large (MinHeap)
        self.small, self.large = [], []
    
    def insertion(self, num: int):
        # push to the max heap and swap with min heap if needed. [IF both are not empty and Small/MaxHeap's max value is greater than Large/Min heap's smallest value]
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # handle uneven sizes
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
    
    def getMedian(self) -> float:
        # if sizes are unequal return biggest length heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2

        
        
    



class main:
    def __init__(self):
        hpq = heap()
        hpq.push(10)
        hpq.push(13)
        hpq.push(5)
        print("\n[HEAP/PRIORITY QUEUE]\nPushed 10, 13, 5 at init in heap respectively")
        print("Heap top: (expected 5): ", hpq.pop())
        print("Heap top: (expected 10): ", hpq.pop())
        print("Heap top: (expected 13): ", hpq.pop())

        print("\n[Heapifying arr = 3,6,2,5]")
        arr = [3, 6, 2, 5]
        hpq.heapify(arr)
        hpq.printHeap()

        print("\n[MEDIAN PROBLEM arr = 3,6,2,5 (expected median 4) and arr2 = 3,6,2,5,1 (expected median 3)]")
        arr = [3, 6, 2, 5]
        arr2 = [3, 6, 2, 5, 1]
        med1 = Median()
        for i in arr:
            med1.insertion(i)
        med2 = Median()
        for i in arr2:
            med2.insertion(i)
        print("Median for first arr: ",med1.getMedian())
        print("Median for second arr: ",med2.getMedian())
        

if __name__ == "__main__":
    main()