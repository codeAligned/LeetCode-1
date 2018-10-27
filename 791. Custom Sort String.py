# 791. Custom Sort String
# Time: O(len(S) + len(T))
# Space: O(len(T))

from collections import Counter

# use Counter to count letter in T and reorder as S
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        cnt_t = Counter(T)
        res = []
        for l in S:
            if l in cnt_t:
                res += [l] * cnt_t[l] # reorder as S
                cnt_t.pop(l)
        for l, cnt in cnt_t.items(): # append leftover in T
            res += [l] * cnt
        return ''.join(res)