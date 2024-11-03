# Used max heap to solve https://leetcode.com/problems/last-stone-weight/
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: # type: ignore
        if len(stones) == 1: return stones[0]
        finalStone = 0
        maxHeap = [ -1 * stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1
            if y - x > 0:
                heapq.heappush(maxHeap, -1 * (y - x))
        
        return 0 if len(maxHeap) == 0 else -1 * heapq.heappop(maxHeap)