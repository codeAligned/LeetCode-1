# 739. Daily Temperatures
# Time: O(N)
# Space: O(N)

# maintain a decreasing stack with value and index, and calculate the index diff
# similar to 503. Next Greater Element II
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(T)
        for i, num in enumerate(T):
            while stack and num > stack[-1][0]:
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append((num, i))
            
        return res
