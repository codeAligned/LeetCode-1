// 485. Max Consecutive Ones
// TIme: O(N)
// Space: O(1)

// iterate and keep track of max value
public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0, max = 0;
        for (int num : nums) {
            if (num == 1) {
                cnt += 1;
            } else {
                cnt = 0;
            }
            max = Math.max(max, cnt);
        }
        return max;
    }
}