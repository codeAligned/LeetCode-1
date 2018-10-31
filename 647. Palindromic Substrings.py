# 647. Palindromic Substrings
# Time: O(N^2)
# Space: O(1)

# count palindromic substrings from the middle to both ends.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def count_palindromic(left, right):
            cnt = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    cnt += 1
                else:
                    break
                left -= 1
                right += 1
            return cnt

        cnt = 0
        for i in range(len(s)): # for each index, check for odd length and even length
            cnt += 1 + count_palindromic(i - 1, i + 1) + count_palindromic(i, i + 1)
        return cnt


# Time: O(N^2)
# Space: O(N^2)

# outer dp results depends on inner ones.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                # record if str slice starting j ending i a palindromic substring
                dp[j][i] = s[j] == s[i] and (i - j < 3 or dp[j+1][i-1])
                if dp[j][i]:
                    res += 1
        return res
