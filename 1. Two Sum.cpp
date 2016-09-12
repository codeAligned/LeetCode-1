// Time:  O(n)
// Space: O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // key is the number and value is its index in the vector
        unordered_map<int, int> hash;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            int numToFind = target - nums[i];
            
            // if numToFind is found in map, return them
            if (hash.find(numToFind) != hash.end()) {
                result.push_back(hash[numToFind]);
                result.push_back(i);
                return result;
            }
            
            hash[nums[i]] = i;
        }
        
        return result;
    }
};