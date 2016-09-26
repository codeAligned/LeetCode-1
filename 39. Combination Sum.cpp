// 39. Combination Sum.cpp
// Time:  O(n!)
// Space: O(n^2)

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> temp;
        Helper(candidates, temp, target, 0, result);
        return result;
    }
    // backtracking
    void Helper(vector<int>& candidates, vector<int>& temp, int target, int begin, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(temp);
            return ;
        } else if (target < 0) { // over sum
            return ;
        }
        // sum more
        for (int i = begin; i < candidates.size(); i++) {
            temp.push_back(candidates[i]);
            Helper(candidates, temp, target - candidates[i], i, result);
            temp.pop_back();
        }
    }
};
