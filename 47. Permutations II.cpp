// 47. Permutations II
// Time:  O(n!)
// Space: O(n^2)

// count same number in order not to repermutations
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;
        unordered_map<int, int> numCount;
        for (int i : nums) {
            if (numCount.find(i) == numCount.end()) 
                numCount[i] = 0;
            numCount[i] += 1;
        }
        Helper(nums, 0, result, temp, numCount);
        return result;
    }
    // backtracking with map to count each number
   void Helper(vector<int>& nums, int begin, vector<vector<int>>& result, vector<int>& temp, unordered_map<int, int>& numCount) {
        if (begin == nums.size()) {
            // one permutation instance
            result.push_back(temp);
            return;
        }
        
        for (auto& p : numCount) {
            if (p.second == 0)
                continue;
            --p.second;
            temp.push_back(p.first);
            Helper(nums, begin + 1, result, temp, numCount);
            // reset
            ++p.second;
            temp.pop_back();
        }
    }
};

