# 521. Longest Uncommon Subsequence I
# Time: O(N)
# Space: O(1)

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return max(len(a), len(b)) if a != b else -1
