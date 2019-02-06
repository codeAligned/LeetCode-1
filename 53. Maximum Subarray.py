# 53. Maximum Subarray
# Time:  O(n)
# Space: O(1)

# dp
# 典型的DP题：
# 1. 状态dp[i]：以A[i]为最后一个数的所有max subarray的和。
# 2. 通项公式：dp[i] = dp[i-1]<=0 ? A[i] : dp[i-1]+A[i]
# 3. 由于dp[i]仅取决于dp[i-1]，所以可以仅用一个变量来保存前一个状态，而节省内存。
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        cur_max = nums[0]
        all_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            all_max = max(cur_max, all_max)
        
        return all_max
