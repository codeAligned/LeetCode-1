// 344. Reverse String
// Time: O(N)
// Space: O(N)

// use StringBuffer reverse method
public class Solution {
    public String reverseString(String s) {
        StringBuffer sb = new StringBuffer(s);
        return sb.reverse().toString();
    }
}