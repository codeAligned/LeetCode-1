# 566. Reshape the Matrix
# Time: O(r * c)
# Space: O(c)

# loop over matrix and add to new matrix row by row
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0]) if m else 0
        if r * c != m * n:
            return nums
        res = []
        row = []
        for i in range(m):
            for j in range(n):
                row.append(nums[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res        
