// Time:  O(n!)
// Space: O(n)

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> temp;
        Helper(n, k, 1, temp, result);
        return result;
    }
    
    // backtracking
    void Helper(int n, int k, int begin, vector<int>& temp, vector<vector<int>>& result) {
        if (k <= 0) {
            result.push_back(temp);
            return ;
        }
        else {
            for (int i = begin; i <= n; ++i) {
                temp.push_back(i);
                Helper(n, k - 1, i + 1, temp, result);
                temp.pop_back();
            }
        }
    }
};