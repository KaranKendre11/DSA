a = [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1]
prev_val = -1
res = []
for i, y in enumerate(a):
    if (prev_val == -1 and y == 1) or (y == 1 and prev_val != -1 and i - prev_val >= 3):
        res.append(i+1) # for 1-indexing
        prev_val = i

print(res)


def maxSubarraySum(arr):
    
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Find the maximum sum ending at index i by either extending 
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update res if maximum subarray sum ending at index i > res
        res = max(res, maxEnding)
    
    return res
