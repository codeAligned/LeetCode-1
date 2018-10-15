# 503. Next Greater Element II
# Time: O(N)
# Space: O(N)

# maintain a decreasing stack, and use % to circulate array
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = [-1] * size
        stack = []
        for i in range(2 * size - 1, -1, -1): # each element only need to look up in the decreasing stack
            while stack and nums[i%size] >= stack[-1]:
                stack.pop() # pop out all the smaller or equal elements
            if stack:
                res[i%size] = stack[-1]
            stack.append(nums[i%size])
        return res
