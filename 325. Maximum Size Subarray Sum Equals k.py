# 325. Maximum Size Subarray Sum Equals k
# Time:  O(N)
# Space: O(N)

# use a map to track up to index array sum and index mappings
class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_idx_dict = {}
        sum = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum += num
            if sum == k: # all up to i array sum equals k
                max_len = i + 1
            elif sum - k in sum_idx_dict: # sub-array up to i sum equals k
                max_len = max(max_len, i - sum_idx_dict[sum-k])
            if sum not in sum_idx_dict: # only keep the shortest up to i array sum to subtract
                sum_idx_dict[sum] = i
        
        return max_len
