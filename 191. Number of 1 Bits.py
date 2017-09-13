# 191. Number of 1 Bits
# Time:  O(1)
# Space: O(1)

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            if n % 2:
                cnt += 1
            n /= 2
        return cnt

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            cnt += n & 1
            n >>= 1
        return cnt
