# 700. Search in a Binary Search Tree
# Time: O(log(N))
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# use a cur pointer to find target val
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        cur = root if root else None
        while cur:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
            else:
                return cur
        return None
