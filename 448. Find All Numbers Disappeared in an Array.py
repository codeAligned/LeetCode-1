# 448. Find All Numbers Disappeared in an Array
# Time: O(N)
# Space: O(N)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        res = []
        for i in nums:
            s.add(i)
        for i in range(1, len(nums) + 1):
            if i not in s:
                res.append(i)
        return res


# Time: O(N)
# Space: O(1)

# take value as index and negate to indicate existence
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
            
        return res
