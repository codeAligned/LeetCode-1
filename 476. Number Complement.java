// 476. Number Complement
// Time: O(1)
// Space: O(1)

// Integer.highestOneBit() can be used
public class Solution {
    public int findComplement(int num) {
        int bits = 0, temp = num;
        while (temp != 0) {
            temp >>= 1;
            bits += 1;
        }
        return ~num & (-1 >>> (32 - bits));
    }
}