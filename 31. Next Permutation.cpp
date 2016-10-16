// 31. Next Permutation
// Time: O(N)
// Space: O(1)

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int k = -1;
        // Find the largest index k such that nums[k] < nums[k + 1]
    	for (int i = nums.size() - 2; i >= 0; i--) {
    		if (nums[i] < nums[i + 1]) {
    			k = i;
    			break;
    		}
    	} 
    	// If no such index exists, the permutation is the last permutation
    	if (k == -1) {
    	    reverse(nums.begin(), nums.end());
    	    return;
    	}
    	int l = -1;
    	// Find the largest index l greater than k such that nums[k] < nums[l]
    	for (int i = nums.size() - 1; i > k; i--) {
    		if (nums[i] > nums[k]) {
    			l = i;
    			break;
    		} 
    	} 
    	// Swap the value of nums[k] with that of nums[l]
    	swap(nums[k], nums[l]);
    	// Reverse the sequence from nums[k + 1] up to and including the final element nums[n].
    	reverse(nums.begin() + k + 1, nums.end()); 
    }
};

