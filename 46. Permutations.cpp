// Time:  O(n!)
// Space: O(n^2)

// DFS recursive
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
	    vector<vector<int>> result;
	    vector<int> temp;
	    Helper(nums, 0, result, temp);
	    return result;
    }
    
    // Basic idea: permutation of A[1..n] equals to
    // A[1] + permutation of (A[1..n] - A[1])
    // A[2] + permutation of (A[1..n] - A[2])
    // ...
    // A[n] + permutation of (A[1..n] - A[n]).
    // backtracking
	void Helper(vector<int>& nums, int begin, vector<vector<int>>& result, vector<int>& temp) {
		if (begin == nums.size()) {
		    // one permutation instance
		    result.push_back(nums);
		    return;
		}
		
		for (int i = begin; i < nums.size(); ++i) {
		    swap(nums[begin], nums[i]);
		    Helper(nums, begin + 1, result, temp);
		    // reset
		    swap(nums[begin], nums[i]);
		}
    }
};