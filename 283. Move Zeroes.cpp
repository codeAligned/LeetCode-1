// Time:  O(n)
// Space: O(1)

// Solution 1
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int insertPos = 0;
        for (auto & num: nums) {
            if (num) {
                swap(nums[insertPos++], num);
            }
        }
    }
};

// Solution 2
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int insertPos = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[insertPos++] = nums[i];
            }
        }
        while(insertPos < nums.size())
            nums[insertPos++] = 0;
    }
};