# 149. Max Points on a Line
# Time:  O(n^2)
# Space: O(n)

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxPoints = 0
        for i, start in enumerate(points):
            slopes, overlap = {}, 1
            for j in xrange(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    overlap += 1
                else:
                    slope = float("inf")
                    if start.x - end.x != 0:
                        slope = (start.y - end.y) * 1.0 / (start.x - end.x)
                    if slope not in slopes:
                        slopes[slope] = 1
                    else:
                        slopes[slope] += 1
            
            curMax = overlap            
            for slope in slopes:
                curMax = max(curMax, slopes[slope] + overlap)
                
            maxPoints = max(maxPoints, curMax)
            
        return maxPoints
                    