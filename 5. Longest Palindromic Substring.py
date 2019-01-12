# 5. Longest Palindromic Substring
# Time:  O(N)
# Space: O(1)

# probe by odd and even length palindromic substring
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        res = ''
        for i, c in enumerate(s):
            p = 0
            while i - p >= 0 and i + p < l: # probe by odd length 
                if s[i-p] == s[i+p]:
                    if 2 * p + 1 >= len(res):
                        res = s[i-p:i+p+1]
                    p += 1
                else:
                    break
            
            if i + 1 < l and c == s[i+1]: # probe by even length
                p = 0
                while i - p >= 0 and i + 1 + p < l:
                    if s[i-p] == s[i+1+p]:
                        if 2 * p + 2 >= len(res):
                            res = s[i-p:i+1+p+1]
                        p += 1
                    else:
                        break

        return res
