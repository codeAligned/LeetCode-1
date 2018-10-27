# 766. Toeplitz Matrix
# Time: O(len(matrix))
# Space: O(1)

# move one column to compare with next row
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0]) if M else 0
        for i in range(M-1):
            if matrix[i][:N-1] != matrix[i+1][1:]:
                return False
        return True
