# 461. Hamming Distance
# Time: O(len(binary digits))
# Space: O(1)

# use XOR operation to get the diff digits and shift bits
class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        xor = x ^ y
        cnt = 0
        while xor != 0:
            if (xor & 1) == 1:
                cnt += 1
            xor >>= 1
        return cnt
