# 1. Two Sum
# Time:  O(N)
# Space: O(N)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buf = {}
        for i, num in enumerate(nums):
            numToFind = target - num
            if numToFind in buf:
                return [buf[numToFind], i]
            else:
                buf[num] = i
        return [];
