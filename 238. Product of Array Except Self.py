# 238. Product of Array Except Self
# Time:  O(N)
# Space: O(1)

# get product from both side
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        left = 1
        for i in range (1, len(nums)): # from left to right get up to left product
            left *= nums[i-1]
            res[i] = left
        
        right = 1
        for i in range (len(nums) - 2, -1, -1): # from right to left get down to right product
            right *= nums[i+1]
            res[i] = res[i] * right
        
        return res
