# 897. Increasing Order Search Tree
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# use recursive to inorder traversal and bulid right nodes tree
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []
        self.inorder(root, res)
        cur = new_root = TreeNode(0)
        for v in res:
            cur.right = TreeNode(v)
            cur = cur.right
        return new_root.right
        
    def inorder(self, root, res):
        if not root:
            return None
        if root.left:
            self.inorder(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right, res)


# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# use stack and cur pointers to iterative inorder traversal and build right nodes tree
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        new_root = new_cur = TreeNode(0)
        stack = []
        cur = root if root else None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            new_cur.right = TreeNode(node.val)
            new_cur = new_cur.right
            if node.right:
                cur = node.right
        return new_root.right
