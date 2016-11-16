# 34. Search for a Range
# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if target == nums[mid]:
                left = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                right = mid
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        return [-1, -1]