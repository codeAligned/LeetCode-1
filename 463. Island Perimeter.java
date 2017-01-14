// 463. Island Perimeter
// Time: O(N^2)
// Space: O(1)

// island plus 4, neighbor minus 2
public class Solution {
    public int islandPerimeter(int[][] grid) {
        int peri = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    peri += 4;
                    if (i > 0 && grid[i-1][j] == 1) peri -= 2;
                    if (j > 0 && grid[i][j-1] == 1) peri -= 2;
                }
            }
        }
        return peri;
    }
}