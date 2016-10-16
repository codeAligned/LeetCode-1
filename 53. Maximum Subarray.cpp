// 53. Maximum Subarray
// Time:  O(n)
// Space: O(1)

// dp
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
