# 28. Implement strStr()
# Time: O(N*len(needle))
# Space: O(k)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            if needle == haystack[i:i + length]:
                return i
        return -1