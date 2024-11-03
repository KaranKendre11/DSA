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


class main:
    def __init__(self):
        minHeap = heap()
        # let's assume we have this array 6,5,4,3,2,1
        arr = [6,5,4,3,2,1]
        # now using insertion we insert elements to build a min heap
        for num in arr:
            minHeap.push(num)
        
        print(minHeap.heap[1:])


if __name__ == "__main__":
    main()