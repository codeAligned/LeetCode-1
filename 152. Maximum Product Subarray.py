# 152. Maximum Product Subarray
# Time:  O(n)
# Space: O(1)

# record cur_max and cur_min for next dp item
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        
        pre_max = nums[0]
        pre_min = nums[0]
        all_max = nums[0]
        for i in range(1, length):
            cur_max = max(max(pre_max * nums[i], pre_min * nums[i]), nums[i])
            cur_min = min(min(pre_max * nums[i], pre_min * nums[i]), nums[i])
            all_max = max(all_max, cur_max)
            pre_max = cur_max
            pre_min = cur_min

        return all_max
