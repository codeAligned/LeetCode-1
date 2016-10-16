// 81. Search in Rotated Sorted Array II
// Time: O(logn)
// Space: O(1)

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        int mid;
        while (start <= end) {
            mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return true;
            }
            if (nums[start] < nums[mid]) {
                if (nums[start] <= target && target < nums[mid])
                    end = mid;
                else
                    start = mid + 1;
            } else if (nums[start] > nums[mid]) {
                if (nums[mid] < target && target <= nums[end])
                    start = mid + 1;
                else
                    end = mid;
            } else {
                // skip the duplicates
                start++;
            }
        }
        return false;
    }
};

