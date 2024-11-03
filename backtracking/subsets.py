# Used backtracking algorithm to solve https://leetcode.com/problems/subsets/ and https://leetcode.com/problems/subsets-ii/

def subsetsWithoutDuplicates(nums):
    subsets, curSet = [], []
    helper(0, nums, subsets, curSet)   
    return subsets

def helper(i, nums, subsets, curSet):
    if i == len(nums):
        subsets.append(curSet.copy())
        return
    
    # Choice 1 include nums[i]
    curSet.append(nums[i])
    helper(i+1, nums, subsets, curSet)
    curSet.pop()
    
    # Choice 2 not include nums[i] , popped nums[i] in the above line
    helper(i+1, nums, subsets, curSet)

def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, curSet = [], []

    helper2(0, nums, subsets, curSet)
    return subsets

def helper2(i, nums, subsets, curSet):
    if i == len(nums):
        subsets.append(curSet.copy())
        return
    
    # choice 1 include nums[i]
    curSet.append(nums[i])
    helper2(i+1, nums, subsets, curSet)
    curSet.pop()

    # choice 2 increament i till nums[i+1] is different from nums[i]
    while i + 1 < len(nums) and nums[i] == nums[i+1]:
        i += 1
    helper2(i+1, nums, subsets, curSet)



def main():
    subsets = subsetsWithoutDuplicates([1,2,3])
    print("Subsets of [1, 2, 3]")
    print(subsets)
    subsets = subsetsWithDuplicates([1,2,2,3])
    print("\nSubsets of [1, 2, 2, 3] (input has duplicates)")
    print(subsets)

if __name__ == "__main__":
    main()


"""
    Example Walkthrough 
    Let's see how the algorithm works with an example, nums = [1, 2]:

    Start with i = 0, curSet = [].
    - Include nums[0]:
        curSet = [1]
        Call helper(1, nums, subsets, curSet)
    - Include nums[1]:
        curSet = [1, 2]
        Call helper(2, nums, subsets, curSet)
        i == 2, append [1, 2] to subsets, backtrack (curSet = [1]) **
    - Exclude nums[1]:
        curSet = [1]
        Call helper(2, nums, subsets, curSet)
        i == 2, append [1] to subsets, backtrack (curSet = []) **
    - Exclude nums[0]:
        curSet = []
        Call helper(1, nums, subsets, curSet)
    - Include nums[1]:
        curSet = [2]
        Call helper(2, nums, subsets, curSet)
        i == 2, append [2] to subsets, backtrack (curSet = []) **
    - Exclude nums[1]:
        curSet = []
        Call helper(2, nums, subsets, curSet)
        i == 2, append [] to subsets, backtracking returns **
    
    The final subsets list will be [ [1, 2], [1], [2], [] ].

    This is how the backtracking algorithm systematically explores all possible subsets of the given list.

"""