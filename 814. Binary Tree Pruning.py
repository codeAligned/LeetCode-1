# 814. Binary Tree Pruning
# Time:  O(N^k)
# Space: O(N^k)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive prune left and right sub-trees until root is None
class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        return root if root.val != 0 or root.left or root.right else None