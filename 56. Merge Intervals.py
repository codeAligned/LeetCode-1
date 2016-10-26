# 56. Merge Intervals
# Time: O(NlogN)
# Space: O(N)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        si = sorted(intervals, key=lambda x: x.start)
        i = 0
        while i < len(si) - 1:
            if si[i].end >= si[i+1].start:
                si[i].end = max(si[i].end, si[i+1].end)
                del si[i+1]
            else:
                i += 1
        
        return si