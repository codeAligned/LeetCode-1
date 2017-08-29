# 561. Array Partition I
# Time:  O(NlogN)
# Space: O(logN)

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in sorted(nums)[::2]:
            sum += i
        return sum