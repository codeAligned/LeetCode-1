# 522. Longest Uncommon Subsequence II
# Time: O(N^2)
# Space: O(1)

# all() all True return True else False
# any() all False return False else True
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def issubseq(s, t): # 'bcc' is a subsequence of 'blceiocas'
            i = 0
            for c in t:
                if i < len(s) and s[i] == c:
                    i += 1
            return i == len(s)
        
        # 'in' operator for 'iter()', iterator is matched until value 1 is matched:
        #   * t = iter([3, 2, 1, 4, 5])
        #   * 1 in t
        #   * next(t) = 4
        def issubseq2(s, t):
            it = iter(t)
            return all(c in it for c in s)
        
        # sort strs by length so that it only validates issubseq from longer or equal length str
        strs.sort(key=lambda x: -len(x))
        for i, s in enumerate(strs):
            if all(not issubseq(s, t) for j, t in enumerate(strs) if i != j and len(t) >= len(s)):
                return len(s)
        
        return -1
