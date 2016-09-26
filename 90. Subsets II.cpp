// 90. Subsets II.cpp
// Time:  O(n!)
// Space: O(n^2)

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;
        sort(nums.begin(), nums.end());
        Helper(nums, temp, 0, result);
        return result;
    }
    // backtracking
    void Helper(vector<int>& nums, vector<int>& temp, int begin, vector<vector<int>>& result) {
        result.push_back(temp);
        for (int i = begin; i < nums.size(); ++i) {
            if(i > begin && nums[i] == nums[i - 1]) // skip duplicates
                continue;
            temp.push_back(nums[i]);
            Helper(nums, temp, i + 1, result);
            temp.pop_back();
        }
    }
};
