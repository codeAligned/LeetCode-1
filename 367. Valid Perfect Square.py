# 367. Valid Perfect Square
# Time: O(logN)
# Space: O(1)

# binary search
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 1, (num >> 1) + 1
        while start <= end:
            mid = (start + end) >> 1
            squre = mid * mid
            if squre == num:
                return True
            if squre > num:
                end = mid - 1
            else:
                start = mid + 1
        return False
