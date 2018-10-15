# 867. Transpose Matrix
# Time: O(N)
# Space: O(1)

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))