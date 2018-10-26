# 6. ZigZag Conversion
# Time: O(N)
# Space: O(N)

# use a boolean to control down and up
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        res = [[] for i in range(numRows)]
        down = True
        rowIndex = 0
        
        for c in s:
            res[rowIndex].append(c)
            if down:
                rowIndex += 1
            else:
                rowIndex -= 1
            if rowIndex == numRows:
                down = False
                rowIndex -= 2
            elif rowIndex == -1:
                down = True
                rowIndex += 2

        return ''.join([''.join(row) for row in res])
