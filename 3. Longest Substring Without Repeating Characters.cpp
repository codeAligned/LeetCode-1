// 3. Longest Substring Without Repeating Characters
// Time:  O(n)
// Space: O(1)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1); // record character index
        int maxLen = 0;
        int start = -1;
        for (int i = 0; i < s.length(); i++) {
            if (dict[s[i]] > start) { // duplicated
                start = dict[s[i]]; // set new start
            }
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
    }
};

