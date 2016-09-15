// Time:  O(logn)
// Space: O(1)

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        int mid;
        int left, right;
        while (start <= end) { // binary search to hit target
            mid = start + (end - start) / 2;
            if (target == nums[mid]) { // move to boundary
                left = mid;
                while (left >= 0 && nums[left] == target)
                    --left;
                ++left;
                right = mid;
                while (right < nums.size() && nums[right] == target)
                    ++right;
                --right;
                return {left, right};
            }
            if (target < nums[mid]) 
                end = mid - 1;
            else
                start = mid + 1;
        }
        return {-1, -1};
    }
};