# 186. Reverse Words in a String II
# Time:  O(N)
# Space: O(1)

class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        start = 0
        for i, c in enumerate(str):
            if c == ' ':
                str[start:i] = str[start:i][::-1]
                start = i+1
        str[start:] = str[start:][::-1]
