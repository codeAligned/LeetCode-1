# 575. Distribute Candies
# Time: O(N)
# Space: O(N)

# min of half of the candies and kinds of candies
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) / 2)
