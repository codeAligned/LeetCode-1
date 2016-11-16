# 1. Two Sum
# Time:  O(n)
# Space: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # key is the number and value is its index in the vector
        buf = {}
        for i, num in enumerate(nums):
            num_to_find = target - num
            
            # if num_to_find is found in map, return them
            if num_to_find in buf:
                return [buf[num_to_find], i]
            else:
                buf[num] = i;
        
        return [];