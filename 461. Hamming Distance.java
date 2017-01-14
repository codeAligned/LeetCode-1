// 461. Hamming Distance
// Time: O(1)
// Space: O(1)

// traverse bit and compare
public class Solution {
    public int hammingDistance(int x, int y) {
        int dis = 0;
        while (x != 0 || y != 0) {
            if ((x & 1) != (y & 1)) {
                dis += 1;
            }
            x >>>= 1;
            y >>>= 1;
        }
        return dis;
    }
}