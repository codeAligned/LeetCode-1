# 283. Move Zeroes
# Time: O(N)
# Space: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        idx = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                nums[idx] = num # move all non-zeros elements advance
                idx += 1
        
        for j in range(idx, idx + zeros):
            nums[j] = 0
        