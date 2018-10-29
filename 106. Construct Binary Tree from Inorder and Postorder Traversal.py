# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursively find the next positions of left and right sub-tree in inorder and postorder sequence.
# inorder: (9,) 3, (15, 20, 7)
# postorder: (9,) (15, 7, 20,) 3
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        root_idx_in_inorder = inorder.index(postorder[-1])
        left_in_inorder = inorder[:root_idx_in_inorder]
        left_in_postorder = postorder[:root_idx_in_inorder]
        root.left = self.buildTree(left_in_inorder, left_in_postorder)
        right_in_inorder = inorder[root_idx_in_inorder+1:]
        right_in_postorder = postorder[root_idx_in_inorder:-1]
        root.right = self.buildTree(right_in_inorder, right_in_postorder)
        return root
