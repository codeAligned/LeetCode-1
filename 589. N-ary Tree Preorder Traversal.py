# 589. N-ary Tree Preorder Traversal
# Time: O(N)
# Space: O(N)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# recursive parent->left->right
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.pre(root, res)
        return res
        
    def pre(self, node, res):
        if not node:
            return None
        res.append(node.val)
        for child in node.children:
            self.pre(child, res)


# Time: O(N)
# Space: O(N)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# iterative with stack (root->pop/visit root->push right->push left)
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = [root] if root else []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack += cur.children[::-1]
        return res
