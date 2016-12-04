# 274. H-Index
# Time: O(NlogN)
# Space: O(1)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(key=lambda x: -x)
        for i, v in enumerate(citations):
            if v < i + 1:
                return i
        return len(citations)