# 91. Decode Ways
# Time: O(N)
# Space: O(1)

from collections import deque

# induction rule: dp[i] = dp[i+1] + dp[i+2]
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i], valid ways starting from i, overrange dp[n] = 1
        dp = deque([1, 1, 1]) # keep dp array O(1)
        for i in range(len(s) - 1, -1, -1): # bottom up dp
            dp.appendleft(0)
            dp.pop()
            digit = int(s[i])
            if digit > 0 and digit < 10: # one digit within 1-9, valid
                dp[0] += dp[1]
            digits = int(s[i:i+2]) # two digits within 10-26, valid
            if digits >= 10 and digits <= 26:
                dp[0] += dp[2]
        return dp[0]
