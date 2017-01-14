// 448. Find All Numbers Disappeared in an Array
// Time: O(N)
// Space: O(1)

// take value as index and negate to indicate existence
public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int idx = Math.abs(nums[i]) - 1;
            if (nums[idx] > 0)
                nums[idx] = -nums[idx];
        }
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] >= 0) {
                res.add(j+1);
            }
        }
        return res;
    }
}