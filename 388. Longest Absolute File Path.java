// 388. Longest Absolute File Path
// Time:  O(n)
// Space: O(n)

// dynamic programming to keep track of the current max length
public class Solution {
    public int lengthLongestPath(String input) {
        int maxLen = 0;
        Map<Integer, Integer> depthLen = new HashMap();
        depthLen.put(0, 0);
        for (String line : input.split("\n")) {
            String name = line.substring(line.lastIndexOf("\t") + 1);
            int depth = line.length() - name.length();
            if (name.contains(".")) {
                maxLen = Math.max(maxLen, depthLen.get(depth) + name.length());
            } else {
                depthLen.put(depth + 1, depthLen.get(depth) + name.length() + 1);
            }
        }
        return maxLen;
    }
}
