# 219. Contains Duplicate II
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


# Time: O(N)
# Space: O(k)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ksize_set = set()
        for i, num in enumerate(nums):
            if num in ksize_set:
                return True
            else:
                ksize_set.add(num)
            if i >= k: # keep k size sliding set
                ksize_set.remove(nums[i - k])
        
        return False
