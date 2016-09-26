// 290. Word Pattern.cpp
// Time:  O(n)
// Space: O(n)

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        istringstream in(str);
        string s;
        vector<string> vs;
        while(in >> s) // split str
            vs.push_back(s);
        if (pattern.size() != vs.size())
            return false;
        map<string, char> s2c;
        map<char, string> c2s;
        for (int i = 0; i < vs.size(); ++i) {
            if (s2c[vs[i]] == 0 && c2s[pattern[i]] == "") { // bijection
                s2c[vs[i]] = pattern[i]; 
                c2s[pattern[i]] = vs[i]; 
            } else if (s2c[vs[i]] != pattern[i]) // detect
                return false;
        }
        return true;
    }
};
