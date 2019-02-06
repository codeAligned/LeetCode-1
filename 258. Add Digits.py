# 258. Add Digits
# Time: O(len(binary digits))
# Space: O(1)

# while loop over the number until zero
class Solution:
    def addDigits(self, num: 'int') -> 'int':
        res = 0
        while num != 0:
            res += num % 10
            num //= 10
            if num == 0 and res >= 10: # keep looping if res >= 10
                num = res
                res = 0
        return res
