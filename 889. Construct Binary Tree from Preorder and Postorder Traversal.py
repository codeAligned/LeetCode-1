# 889. Construct Binary Tree from Preorder and Postorder Traversal
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursively find the next positions of left and right sub-tree in pre and post sequence.
# pre: 1, (2, 4, 5, 7,) (3, 6)
# post: (4, 7, 5, 2,) (6, 3,) 1
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        left_idx_in_post = post.index(pre[1])
        left_in_pre = pre[1:1+left_idx_in_post+1]
        left_in_post = post[:left_idx_in_post+1]
        root.left = self.constructFromPrePost(left_in_pre, left_in_post)
        right_in_pre = pre[1+left_idx_in_post+1:]
        right_in_post = post[left_idx_in_post+1:-1]
        root.right = self.constructFromPrePost(right_in_pre, right_in_post)
        return root
