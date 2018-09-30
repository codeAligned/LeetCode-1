# 1. Two Sum
# Time:  O(N)
# Space: O(N)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index_map = {}
        for i, num in enumerate(nums):
            to_find = target - num
            if to_find not in num_index_map:
                num_index_map[num] = i
            else:
                return [num_index_map[to_find], i]
            