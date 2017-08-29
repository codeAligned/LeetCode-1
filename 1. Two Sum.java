// 1. Two Sum
// Time:  O(n)
// Space: O(n)

// HashMap to keep track of current to find number
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int toFind = target - nums[i];
            if (m.containsKey(toFind)) {
                return new int[] { m.get(toFind), i };
            }
            m.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
