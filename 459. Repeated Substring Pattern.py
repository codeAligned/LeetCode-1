# 459. Repeated Substring Pattern
# Time: O(N^2)
# Space: O(1)

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        for i in range(1, len(str) // 2 + 1):
            flag = True
            for j in range(i, len(str), i):
                sub = str[0:i]
                if str[j:j+i] != sub:
                    flag = False
                    break
            if flag:
                return True
        return False