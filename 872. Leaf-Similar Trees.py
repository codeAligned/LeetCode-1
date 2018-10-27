# 872. Leaf-Similar Trees
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# use preorder (stack with right then left) to track leaf node
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1, res2 = [], []
        self.preorder(root1, res1)
        self.preorder(root2, res2)
        return res1 == res2
        
    def preorder(self, root, res):
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not (node.left or node.right):
                res.append(node.val)
        print(res)
