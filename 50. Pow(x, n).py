# 50. Pow(x, n)
# Time:  O(1)
# Space: O(1)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1
        if n < 0:
            x = 1 / x
            n = -n
    	while n: # bit manipulation
    	    if n & 1:
    	        ans *= x
    	    x *= x
    	    n >>= 1
    	return ans;