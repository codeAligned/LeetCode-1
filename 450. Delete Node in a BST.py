# 450. Delete Node in a BST
# Time: O(Height)
# Space: O(Height)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # key == root.val
            if not root.left and not root.right:
                return None
            elif root.left: # FindMax in left sub-tree
                cur = root.left
                while cur.right:
                    cur = cur.right
                root.val = cur.val
                root.left = self.deleteNode(root.left, cur.val)
            else: # FindMin in right sub-tree
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
        return root
            