# 896. Monotonic Array
# Time: O(N)
# Space: O(1)

# decide increasing or decreasing at first to save some time.
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        left = A[0]
        right = A[len(A)-1]
        if right >= left:
            for i, num in enumerate(A[:-1]):
                if A[i+1] < num:
                    return False
        else:
            for i, num in enumerate(A[:-1]):
                if A[i+1] > num:
                    return False
        return True
