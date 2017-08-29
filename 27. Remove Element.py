# 27. Remove Element
# Time: O(N)
# Space: O(1)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                idx += 1
            else:
                cnt += 1
            if idx < len(nums) - cnt:
                nums[idx] = nums[idx + cnt]
            else:
                break
        return idx