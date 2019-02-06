# 20. Valid Parentheses
# Time: O(N)
# Space: O(N)

# use stack and map to match pairs.
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack = []
        p = {'{': '}', '[': ']', '(': ')'}
        for c in s:
            if c in p:
                stack.append(p[c])
            elif len(stack) > 0 and c == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
