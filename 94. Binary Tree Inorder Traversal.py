# 94. Binary Tree Inorder Traversal
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursive left->parent->right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorder(root, res)
        return res
        
    def inorder(self, node, res):
        if not node:
            return None
        if node.left:
            self.inorder(node.left, res)
        res.append(node.val)
        if node.right:
            self.inorder(node.right, res)


# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# iterative with stack and cur pointer
# while stack or cur
# while cur -> push cur -> cur = cur.left
# visit node = stack.pop() -> cur = node.right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        cur = root if root else None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            if node.right:
                cur = node.right
        return res
