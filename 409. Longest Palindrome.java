// 409. Longest Palindrome
// Time: O(N)
// Space: O(N/2)

// use set to count char pairs
public class Solution {
    public int longestPalindrome(String s) {
        if (s == null || s.length() == 0)
            return 0;
        Set<Character> hs = new HashSet<>();
        int cnt = 0;
        for (char c : s.toCharArray()) {
            if (hs.contains(c)) {
                hs.remove(c);
                cnt += 1;
            } else {
                hs.add(c);
            }
        }
        return hs.isEmpty() ? cnt * 2 : cnt * 2 + 1;
    }
}