# 13. Roman to Integer
# Time: (len(s))
# Space: O(1)

# last char always do addition, if two characters, the first one do substraction
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] >= roman[s[i + 1]]: # left >= right, positive
                z += roman[s[i]]
            else: # left < right, negative
                z -= roman[s[i]]
        return z + roman[s[-1]] # last bit must be positive