# 657. Robot Return to Origin
# Time:  O(N)
# Space: O(N)

from collections import Counter

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cnt = Counter(moves)
        return cnt['U'] == cnt['D'] and cnt['L'] == cnt['R']
