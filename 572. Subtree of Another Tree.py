# 572. Subtree of Another Tree
# Time: O(ST)
# Space: O(S)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t: # None is subtree for all trees
            return True
        if not s: # No tree is a subtree of None
            return False
        if s.val == t.val:
            if self.isSameTree(s, t): # Two trees are the same is valid
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) # t can be subtree to s.left or s.right
    
    def isSameTree(self, s, t):
        if not s and not t: # both trees are None are the same
            return True
        if not s or not t: # one tree is None would not be the same
            return False
        if s.val != t.val: # Node value should be the same
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right) # left and right should be the same