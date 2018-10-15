# 652. Find Duplicate Subtrees
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# post order to make label numbers for sub-trees
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.number = 0
        self.subtree_num_map = {}
        self.res = set()
        self.post_order(root)
        return list(self.res)
        
        
    def post_order(self, root):
        if not root:
            return 0
        left_num = self.post_order(root.left)
        right_num = self.post_order(root.right)
        subtree_num = (root.val, left_num, right_num) # use root, left, right to form a label number
        if subtree_num not in self.subtree_num_map:
            self.number += 1
            self.subtree_num_map[subtree_num] = (self.number, root)
            return self.number
        else:
            self.res.add(self.subtree_num_map[subtree_num][1])
            return self.subtree_num_map[subtree_num][0]
