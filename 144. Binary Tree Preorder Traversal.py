# 144. Binary Tree Preorder Traversal
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursive parent->left->right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.pre(root, res)
        return res
    
    def pre(self, node, res):
        if not node:
            return None
        res.append(node.val)
        if node.left:
            self.pre(node.left, res)
        if node.right:
            self.pre(node.right, res)


# Time: O(N)
# Space: O(N)

# dfs iterative using stack
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# iterative with stack (root->pop/visit root->push right->push left)
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root] if root else []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
