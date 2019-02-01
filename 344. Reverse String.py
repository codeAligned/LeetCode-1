# 344. Reverse String
# Time: O(N/2)
# Space: O(1)

# switch the left and right chars until middle
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)//2):
            left = s[i]
            right = s[len(s)-1-i]
            s[i] = right
            s[len(s)-1-i] = left
