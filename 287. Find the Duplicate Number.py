# 287. Find the Duplicate Number
# Time:  O(nlogn)
# Space: O(1)

# binary search and count numbers to look for duplicate number
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1 # look from interval [1:n]
        while low <= high:
            mid = (low + high) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid: # duplicate num in [1:mid-1]
                high = mid - 1
            else: # duplicate num in [mid+1:n]
                low = mid + 1
        
        return low
