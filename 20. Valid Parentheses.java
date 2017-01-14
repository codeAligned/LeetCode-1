// 20. Valid Parentheses
// Time: O(N)
// Space: O(N)

// pair corresponding brackets using stack
public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '[') {
                stack.push(']');
            } eles if (c == '{') {
                stack.push('}');    
            }else if (stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        return stack.isEmpty();
    }
}