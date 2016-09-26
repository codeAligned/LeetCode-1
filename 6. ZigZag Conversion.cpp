// 6. ZigZag Conversion.cpp
// Time:  O(n)
// Space: O(s.length())

class Solution {
public:
    string convert(string s, int numRows) {
        string result = "";
        if (numRows == 1)
			return s;
        int step1,step2, pos;
        int len = s.size();
        for (int i = 0; i < numRows; ++i){
            // generally 2 steps to get next character
            step1 = 2 * numRows - 2 * (i + 1); 
            step2 = 2 * i;
            pos = i;
            if (pos < len)
                result += s[pos]; // add first column
            while(1) { // keep iterating the 2 steps to get characters
                pos += step1;
                if (pos >= len) // detect overflow
                    break;
				if (step1) // last row only has step 2
					result += s[pos];
                pos += step2;
                if (pos >= len)
                    break;
				if(step2) // first row only has step 1
					result += s[pos];
            }
        }
        return result;
    }
};
