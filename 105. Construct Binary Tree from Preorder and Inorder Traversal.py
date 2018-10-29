# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursively find the next positions of left and right sub-tree in preorder and inorder sequence.
# preorder: 3, (9,) (20, 15, 7)
# inorder: (9,) 3, (15, 20, 7)
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        root_idx_in_inorder = inorder.index(preorder[0])
        left_in_preorder = preorder[1:1+root_idx_in_inorder]
        left_in_inorder = inorder[:root_idx_in_inorder]
        root.left = self.buildTree(left_in_preorder, left_in_inorder)
        right_in_preorder = preorder[1+root_idx_in_inorder:]
        right_in_inorder = inorder[root_idx_in_inorder+1:]
        root.right = self.buildTree(right_in_preorder, right_in_inorder)
        return root
