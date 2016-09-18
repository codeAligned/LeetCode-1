// Time:  O(nlogn)
// Space: O(1)

class Solution {
public:
    char findTheDifference(string s, string t) {
        sort(s.begin(), s.end()); // sort two string
        sort(t.begin(), t.end());
        int i;
        for (i = 0; i < s.length(); ++i) {
            if (s[i] != t[i]) // find the first different
                return t[i];
        }
        return t[i];
    }
};