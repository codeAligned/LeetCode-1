# 590. N-ary Tree Postorder Traversal
# Time: O(N)
# Space: O(N)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# recursive left->right->parent
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.post(node, res)
        return res

    def post(self, node, res):
        if not node:
            return None
        for child in node.children:
                self.post(child, res)
        res.append(node.val)


# Time: O(N)
# Space: O(N)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# iterative with stack (root->pop/visit root->push left->push right, return reverse)
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = [root] if root else []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack += [child for child in cur.children]
        return res[::-1]
