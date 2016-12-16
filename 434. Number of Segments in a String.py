# 434. Number of Segments in a String
# Time: O(N)
# Space: O(seg)

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())