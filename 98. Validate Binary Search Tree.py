# 98. Validate Binary Search Tree
# Time: O(N)
# Space: O(logN)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS recursive validate BST
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.helper(root, float('-inf'), float('inf'))
        
    def helper(self, root, min_val, max_val): # use helper to keep track of min and max for the root.val
        if not root:
            return True
        
        if min_val < root.val < max_val:
            return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
        
        return False
