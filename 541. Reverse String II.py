# 541. Reverse String II
# Time: O(N/2)
# Space: O(1)

# iterate every 2k elements
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = list(s)
        print(s_list)
        for i in range(0, len(s), 2 * k):
            if len(s) - 1 - i + 1 < k: # reverse all if less than k left
                s_list[i:] = s_list[i:][::-1]
            else: # reverse first k
                s_list[i:i+k] = s_list[i:i+k][::-1]
        return ''.join(s_list)
