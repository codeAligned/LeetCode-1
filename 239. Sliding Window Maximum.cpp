// Time:  O(k * n)
// Space: O(n)

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        if (nums.empty())
            return result;
        for (int i = 0; i <= nums.size() - k; ++i) {
            int max = numeric_limits<int>::min();
            for (int j = 0; j < k; ++j) {
                if (nums[i + j] > max) {
                    max = nums[i + j];
                }
            }
            result.push_back(max);
        }
        return result;
    }
};


// Time:  O(n), because each element is push or pop once
// Space: O(k)

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> result;
        deque<int> dq;
        for (int i = 0; i < n; ++i) {
            while (!dq.empty() && dq.front() < i - k + 1) // remove numbers out of range k
                dq.pop_front();
            while (!dq.empty() && nums[dq.back()] < nums[i]) // remove numbers less than incoming number
                dq.pop_back();  
            dq.push_back(i);
            if (i >= k - 1) 
                result.push_back(nums[dq.front()]);
        }
        return result;
    }
};