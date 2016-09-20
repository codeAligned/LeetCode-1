// Time:  O(n!)
// Space: O(n^2)

// count same number in order not to repermutations
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> v;
        vector<int> r;
        map<int, int> numCount;
        for (int i : nums) {
            if (numCount.find(i) == numCount.end()) 
                numCount[i] = 0;
            numCount[i]++;
        }
        Helper(v, r, numCount, nums.size());
        return v;
    }

    void Helper(vector<vector<int>> &v, vector<int> &r, map<int, int> &numCount, int n) {
        if (n == 0) {
            v.push_back(r);
            return;
        }
        for (auto &p : numCount) {
            if (p.second == 0) 
                continue;
            p.second--;
            r.push_back(p.first);
            Helper(v, r, numCount, n - 1);
            r.pop_back();
            p.second++;
        }
    }
};