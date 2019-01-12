# 387. First Unique Character in a String
# Time:  O(N)
# Space: O(N)

from collections import Counter

# Counter to get frequency, and iterate once
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_cnt = Counter(s)
        for i, c in enumerate(s):
            if letter_cnt[c] == 1:
                return i
        return -1
        