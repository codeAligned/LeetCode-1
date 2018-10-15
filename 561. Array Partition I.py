# 561. Array Partition I
# Time:  O(NlogN)
# Space: O(1)

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
