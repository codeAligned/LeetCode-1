# 485. Max Consecutive Ones
# Time: O(N)
# Space: O(1)

# use a cnt to accumulate 1s and a max_cnt to record the max length
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cnt = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0
        return max_cnt
