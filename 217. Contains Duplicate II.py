# 217. Contains Duplicate II
# Time: O(N)
# Space: O(N)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}
        for i, num in enumerate(nums):
            if num in m:
                if abs(m[num] - i) <= k:
                    return True
                else:
                    m[num] = i
            else:
                m[num] = i
        return False