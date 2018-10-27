# 463. Island Perimeter
# Time: O(grid)
# Space: O(1)

# consider left/right/up/down 4 directions if grid == 1
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) if grid else 0
        n = len(grid[0]) if grid[0] else 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 1
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 1
                    if i < m - 1 and grid[i+1][j] == 1:
                        res -= 1
                    if j < n - 1 and grid[i][j+1] == 1:
                        res -= 1
        return res
