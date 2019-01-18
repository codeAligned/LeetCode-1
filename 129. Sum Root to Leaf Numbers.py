# 129. Sum Root to Leaf Numbers
# Time: O(logN)
# Space: O(logN)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS recursive to get sum, need to carry num_str and num_sum to append str and get sum
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root, '', 0)

    def helper(self, root, num_str, num_sum):
        if not root.left and not root.right:
            return num_sum + int(num_str + str(root.val))
        left_sum, right_sum = 0, 0
        if root.left:
            left_sum = self.helper(root.left, num_str + str(root.val), num_sum)
        if root.right:
            right_sum = self.helper(root.right, num_str + str(root.val), num_sum)
        return num_sum + left_sum + right_sum
