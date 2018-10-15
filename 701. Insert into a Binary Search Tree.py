# 701. Insert into a Binary Search Tree
# Time: O(Height)
# Space: O(Height)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root


# Time: O(Height)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            elif val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root
