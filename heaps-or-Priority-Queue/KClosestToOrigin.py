# Used min heap and a map to store point and min heap for distance to solve https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: # type: ignore
        minHeap = []
        distMap  = {}
        heapq.heapify(minHeap)
        for point in points:
            dist = math.sqrt( ((0 - point[0]) ** 2) + ((0 - point[1]) ** 2))
            heapq.heappush(minHeap, dist)
            if dist in distMap.keys():
                distMap[dist].append(point)
            else:
                distMap[dist] = [point]    
        ans = []
        while k:
            dist = heapq.heappop(minHeap)
            for point in distMap[dist]:
                ans.append(point)
                k -= 1
        return ans
        