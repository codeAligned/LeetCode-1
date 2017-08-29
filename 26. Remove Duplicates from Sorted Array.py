# 26. Remove Duplicates from Sorted Array
# Time: O(N)
# Space: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums);
        
        idx = 0
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
