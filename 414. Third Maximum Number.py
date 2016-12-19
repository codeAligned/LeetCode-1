# 414. Third Maximum Number
# Time: O(N)
# Space: O(1)

# use min heap to keep track of max three elements
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_three = []
        for i in set(nums):
            if len(max_three) < 3:
                heapq.heappush(max_three, i)
            elif i > max_three[0]:
                heapq.heappushpop(max_three, i)
        
        return max(max_three) if len(max_three) < 3 else max_three[0]
