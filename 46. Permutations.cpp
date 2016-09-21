// Time:  O(n!)
// Space: O(n^2)

// DFS recursive
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
	    vector<vector<int>> result;
	    
	    permuteHelper(nums, 0, result);
	    return result;
    }
    
    // Basic idea: permutation of A[1..n] equals to
    // A[1] + permutation of (A[1..n] - A[1])
    // A[2] + permutation of (A[1..n] - A[2])
    // ...
    // A[n] + permutation of (A[1..n] - A[n]).
    // backtracking
	void permuteHelper(vector<int> &nums, int begin, vector<vector<int>> &result) {
		if (begin == nums.size()) {
		    // one permutation instance
		    result.push_back(nums);
		    return;
		}
		
		for (int i = begin; i < nums.size(); ++i) {
		    swap(nums[begin], nums[i]);
		    permuteHelper(nums, begin + 1, result);
		    // reset
		    swap(nums[begin], nums[i]);
		}
    }
};