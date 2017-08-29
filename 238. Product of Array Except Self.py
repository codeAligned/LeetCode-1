# 238. Product of Array Except Self
# Time:  O(N)
# Space: O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = [1] * length
        begin = 1
        end = 1
        for i in range(length):
            output[i] *= begin;
            begin *= nums[i];
            output[length - 1 - i] *= end;
            end *= nums[length - 1 - i];
        return output
