# 18. 4Sum
# Time: O(N^3)
# Space: O(1)

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        solution_list = []
        nums.sort()
        for i, num1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            rest_nums = nums[i+1:]
            for j, num2 in enumerate(rest_nums):
                if j > 0 and rest_nums[j] == rest_nums[j-1]:
                    continue
                rest_target = target - num1 - num2
                start, end = j + 1, len(rest_nums) - 1
                while start < end:
                    if rest_nums[start] + rest_nums[end] == rest_target:
                        solution_list.append([num1, num2, rest_nums[start], rest_nums[end]])
                        while start < end and rest_nums[start] == rest_nums[start+1]:
                            start += 1
                        while start < end and rest_nums[end] == rest_nums[end-1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif rest_nums[start] + rest_nums[end] < rest_target:
                        start += 1
                    else:
                        end -= 1
                        
        return solution_list