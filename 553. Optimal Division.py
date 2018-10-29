# 553. Optimal Division
# Time: O(N)
# Space: O(N)

# dividend should be largest, while divisor should be smallest
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return '{}/({})'.format(str(nums[0]), '/'.join(map(str, nums[1:]))) if len(nums) > 2 else '/'.join(map(str, nums))
