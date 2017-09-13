# 42. Trapping Rain Water
# Time:  O(N)
# Space: O(N)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n
        water = 0
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i - 1])
        
        for j in range(n - 2, -1, -1):
            rightmax[j] = max(rightmax[j + 1], height[j + 1])
        
        for k in range(1, n - 1):
            minH = min(leftmax[k], rightmax[k])
            if minH > height[k]:
                water += minH - height[k]
        
        return water