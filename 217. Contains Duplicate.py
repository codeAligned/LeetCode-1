# 217. Contains Duplicate
# Time: O(N)
# Space: O(N)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))