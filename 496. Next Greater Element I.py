# 496. Next Greater Element I
# Time: O(N)
# Space: O(N)

# maintain a decreasing stack
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        num_greater_map = {}
        stack = []
        for num in nums:
            while stack and num > stack[-1]:
                num_greater_map[stack.pop()] = num # map num and next greater num
            stack.append(num)
        
        res = []
        for num in findNums:
            res.append(num_greater_map.get(num, -1))
        
        return res
