# 15. 3Sum
# Time: O(N^2)
# Space: O(1)

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution_list = []
        if len(nums) < 3:
            return solution_list
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - num
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    solution_list.append([num, nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1

        return solution_list