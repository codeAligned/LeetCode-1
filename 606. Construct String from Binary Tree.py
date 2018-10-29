# 606. Construct String from Binary Tree
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursive build tree2str, attention to no left only right case.
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        s = str(t.val)
        if t.left:
            s += '({})'.format(self.tree2str(t.left))
        elif t.right: # no left only right case, attach placeholder parentheses
            s += '()'
        if t.right:
            s += '({})'.format(self.tree2str(t.right))
        return s
