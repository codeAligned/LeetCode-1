# 771. Jewels and Stones
# Time:  O(N)
# Space: O(N)

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jew_set = set(J)
        jew_cnt = 0
        for c in S:
            if c in jew_set:
                jew_cnt += 1
        
        return jew_cnt
