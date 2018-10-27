# 884. Uncommon Words from Two Sentences
# Time: O(N)
# Space: O(N)

from collections import Counter

# Counter is defaultdict(int), key not in equals 0
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        cnt_A = Counter(A.split(' '))
        cnt_B = Counter(B.split(' '))
        res = []
        res += [k for k, v in cnt_A.items() if cnt_A[k] == 1 and k not in cnt_B]
        res += [k for k, v in cnt_B.items() if k not in cnt_A and cnt_B[k] == 1]
        return res
