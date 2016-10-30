// 384. Shuffle an Array
// Time:  O(n)
// Space: O(n)

// srand(time(NULL or 0))
// rand() % N

// vector.erase(vector.begin() + k or iter)

class Solution {
    vector<int> nums;
public:
    Solution(vector<int> nums) {
        this->nums = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return nums;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> nums2(nums);
        for (int i = 0;i < nums2.size();i++) {
            int pos = rand() % (nums2.size() - i);
            swap(nums2[i + pos], nums2[i]);
        }
        return nums2;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */