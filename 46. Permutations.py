# 46. Permutations
# Time:  O(n!)
# Space: O(n^2)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Basic idea: permutation of A[1..n] equals to
        # A[1] + permutation of (A[1..n] - A[1])
        # A[2] + permutation of (A[1..n] - A[2])
        # ...
        # A[n] + permutation of (A[1..n] - A[n]).
        # backtracking
        def helper(nums, begin, result):
	        if begin == len(nums):
	            result.append(nums[:])
	            return
		
	    	for i in range(begin, len(nums)):
		        nums[begin], nums[i] = nums[i], nums[begin]
		        helper(nums, begin + 1, result)
		        # reset
		        nums[begin], nums[i] = nums[i], nums[begin]
        
        result = []
        tmep = []
        helper(nums, 0, result)
        return result;
        