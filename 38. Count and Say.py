# 38. Count and Say
# Time: O(n * l)
# Space: O(longest)

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            letter, temp, count = s[0], '', 0
            for l in s:
                if letter == l:
                    count += 1
                else:
                    temp += str(count) + letter
                    letter = l
                    count = 1
            temp += str(count) + letter
            s = temp
        return s
        