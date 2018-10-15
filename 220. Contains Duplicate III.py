# 220. Contains Duplicate III
# Time: O(N)
# Space: O(k)

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or t < 0:
            return False
        buckets = {}
        min_num = min(nums)
        for i, num in enumerate(nums):
            bucket_i = (num - min_num) // (t + 1)
            # within value difference if fall into same bucket
            if bucket_i in buckets:
                return True
            # possibly within value difference if in adjcent bucket
            if bucket_i - 1 in buckets and abs(num - buckets[bucket_i-1]) <= t:
                return True
            if bucket_i + 1 in buckets and abs(num - buckets[bucket_i+1]) <= t:
                return True
            buckets[bucket_i] = num
            # keep sliding window size for the buckets
            if i >= k:
                buckets.pop((nums[i - k] - min_num) // (t + 1))

        return False