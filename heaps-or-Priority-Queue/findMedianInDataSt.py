# Used TWO heaps small (maxHeap) and large (minHeap) to solve  https://leetcode.com/problems/find-median-from-data-stream/
import heapq
class MedianFinder:

    def __init__(self):
        # small is maxHeap (max value of the smallest array) and large is minHeap (min value of the largest array)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # default small but swap with large if needeed (make sure all num in small is <= num in large)
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # handle uneven sizes (if difference is greater than one)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
