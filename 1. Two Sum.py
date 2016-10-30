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
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            
            # if num_to_find is found in map, return them
            if num_to_find in buf:
                return [buf[num_to_find], i]
            else:
                buf[nums[i]] = i;
        
        return [];