# 56. Merge Intervals
# Time:  O(NlogN)
# Space: O(1)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# sort and compare adjacent intervals
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        res = []
        cur_interval = intervals[0]
        for interval in intervals[1:]:
            if interval.start <= cur_interval.end:
                cur_interval.end = max(interval.end, cur_interval.end)
            else:
                res.append(cur_interval)
                cur_interval = interval
        return res + [cur_interval]
