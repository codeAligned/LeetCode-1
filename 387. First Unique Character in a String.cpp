// Time:  O(n)
// Space: O(1)

class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> alphabet(26, 0); // record letter times
        for (int i = 0; i < s.length(); ++i) {
            alphabet[s[i] - 'a'] += 1;
        }
        for (int j = 0; j < s.length(); ++j) {
            if (alphabet[s[j] - 'a'] == 1)
                return j;
        }
        return -1;
    }
};