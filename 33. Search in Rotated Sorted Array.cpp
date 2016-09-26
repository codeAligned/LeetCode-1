// Time:  O(n)
// Space: O(1)

// Solution 1
class Solution {
public:
    int search(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
};


// Time:  O(logn)
// Space: O(1)

// Solution 2
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        int mid;
        while (start <= end) {
            mid = start + (end - start) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[start] <= nums[mid]) {
                if (target < nums[mid] && target >= nums[start])
                    end = mid;
                else
                    start = mid + 1;
            } else {
                if (target > nums[mid] && target <= nums[end])
                    start = mid + 1;
                else
                    end = mid;
            }
        }
        return -1;
    }
};