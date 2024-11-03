# Used prefix and postfix in a single array to solve https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # type: ignore
        res = []
        pre = 1
        for i in range (len(nums)):
            if(len(res) == len(nums)):
                break
            res.append(pre)
            pre *= nums[i]
        
        post = 1
        print(res)
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res