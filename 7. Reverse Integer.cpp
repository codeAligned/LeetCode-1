// Time:  O(1)
// Space: O(1)

class Solution {
public:
    int reverse(int x) {
        int temp = 0;
        int result = 0;
        while (x != 0) {
            temp = result * 10 + x % 10;
            if (temp / 10 != result)
                return 0;
            x /= 10;
            result = temp;
        }
        return result;
    }
};