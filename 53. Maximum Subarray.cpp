// 53. Maximum Subarray
// Time:  O(n)
// Space: O(1)

// dp
// 典型的DP题：
// 1. 状态dp[i]：以A[i]为最后一个数的所有max subarray的和。
// 2. 通项公式：dp[i] = dp[i-1]<=0 ? dp[i] : dp[i-1]+A[i]
// 3. 由于dp[i]仅取决于dp[i-1]，所以可以仅用一个变量来保存前一个状态，而节省内存。
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        else if (nums.size() == 1)
            return nums[0];
            
        int size = nums.size();
        int result, maximum;
        result = nums[0], maximum = nums[0];
        for (int i = 1; i < size; ++i) {
            result = max(result + nums[i], nums[i]);
            maximum = max(maximum, result);
        }
        
        return maximum;
    }
};
