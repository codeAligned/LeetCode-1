// 136. Single Number
// Time: O(N)
// Space: O(1)

public class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int num: nums) {
            res ^= num;
        }
        return res;
    }
}