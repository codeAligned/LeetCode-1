# 503. Next Greater Element II
# Time: O(N)
# Space: O(N)

# maintain a decreasing stack with value and index, and use % to circulate array
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = [-1] * size
        stack = []
        for i in range(2 * size): # iterate array twice
            while stack and nums[i%size] > stack[-1][0]: # larger num incoming
                idx = stack.pop()[1] # keep popping out smaller num's index until stack empty or not larger
                res[idx%size] = nums[i%size] # assign next larger num
            stack.append((nums[i%size], i)) # append the incoming num to the stack
        return res
