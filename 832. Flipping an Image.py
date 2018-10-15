# 832. Flipping an Image
# Time:  O(N*k)
# Space: O(N)

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for row in A:
            reversed_row = []
            for i in range(len(row) - 1, -1, -1):
                reversed_row.append(1 - row[i])
            res.append(reversed_row)
        return res