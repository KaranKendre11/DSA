# Using count hashmap and an 2-d freq array which basically has index as the count hashmap values and an array of keys for that count hashmap values 
# https://leetcode.com/problems/top-k-frequent-elements/description/
# example:
# array = [1, 1, 1, 2, 2, 3] 
# hashmap = {1: 3, 2: 2, 3: 1}
# freq = [[], [3], [2], [1], [], [], [] ] -- this will be the length of the array + 1
# Algorithm used modified bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # type: ignore
        count = {}
        freq = [[] for i in range(0,len(nums)+1)]
        ans = []
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        for key in count.keys():
            freq[count[key]].append(key)
        for values in reversed(freq):
            if k == 0: break
            for value in values:
                ans.append(value)
                k -= 1
        return ans
