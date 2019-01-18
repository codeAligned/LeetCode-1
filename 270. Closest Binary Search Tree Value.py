# 270. Closest Binary Search Tree Value
# Time: O(logN)
# Space: O(logN)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS recursive find out the closest value, don't need to carry anything to find for each node
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root.val == target:
            return root.val
        elif root.val < target:
            if root.right:
                val = self.closestValue(root.right, target)
                return root.val if (target - root.val) < (val - target) else val
            else:
                return root.val
        else:
            if root.left:
                val = self.closestValue(root.left, target)
                return root.val if (root.val - target) < (target - val) else val
            else:
                return root.val
