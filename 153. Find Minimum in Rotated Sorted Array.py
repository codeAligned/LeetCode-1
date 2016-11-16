# 153. Find Minimum in Rotated Sorted Array
# Time: O(logN)
# Space: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = start + (end - start) / 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
                
        return nums[start]