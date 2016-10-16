// 164. Maximum Gap
// Time: O(N)
// Space: O(N)

// bucket sort
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if(nums.size() < 2)
            return 0;
        int maxNum = *max_element(nums.begin(), nums.end());
        int minNum = *min_element(nums.begin(), nums.end());
        //average gap from minNum to maxNum.
        int bucketLen = (maxNum - minNum - 1) / (nums.size() - 1) + 1;
        //number of buckets
        int bucketNum = (maxNum - minNum) / bucketLen + 1;
        vector<int> bucketsMin(bucketNum, INT_MAX);
        vector<int> bucketsMax(bucketNum, INT_MIN);
        //put into buckets
        for(int i = 0; i < nums.size(); i ++) {
            int bucketIdx = (nums[i] - minNum) / bucketLen;
            bucketsMin[bucketIdx] = min(bucketsMin[bucketIdx], nums[i]);
            bucketsMax[bucketIdx] = max(bucketsMax[bucketIdx], nums[i]);
        }
        int maxGap = INT_MIN;
        int previous = minNum;
        for(int i = 0; i < bucketNum; i ++)
        {
            if(bucketsMin[i] == INT_MAX && bucketsMax[i] == INT_MIN)
                continue;   //empty
            maxGap = max(maxGap, bucketsMin[i] - previous);
            previous = bucketsMax[i];
        }
        return maxGap;
    }
};

