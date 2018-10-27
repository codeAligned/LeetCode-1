# 893. Groups of Special-Equivalent Strings
# Time: O(N)
# Space: O(N)

# python str odd/even slicing
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        groups = set()
        for seq in A:
            odd = ''.join(sorted(seq[::2]))
            even = ''.join(sorted(seq[1::2]))
            groups.add((odd, even))
        return len(groups)
