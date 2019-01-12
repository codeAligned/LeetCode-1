# 1. Two Sum
# Time:  O(N)
# Space: O(N)

# use a map to track number index mappings
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index_map = {}
        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in nums_index_map:
                return [nums_index_map[to_find], i]
            else:
                nums_index_map[num] = i
