# 485. Max Consecutive Ones
# Time: O(N)
# Space: O(1)

# use a cnt to accumulate 1s and a max_cnt to record the max length
class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int':
        max_cnt = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
        return max_cnt
