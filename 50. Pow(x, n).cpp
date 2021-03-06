// 50. Pow(x, n)
// Time:  O(1)
// Space: O(1)

class Solution {
public:
    double myPow(double x, int n) {
    	double ans = 1;
    	unsigned long long p;
    	if (n < 0) {
    		p = -n;
    		x = 1 / x;
    	} else {
    		p = n;
    	}
		while (p) { // bit manipulation
			if (p & 1)
				ans *= x;
			x *= x;
			p >>= 1;
		}
		return ans;
    }
};

