# 199. Binary Tree Right Side View
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bfs level order traversal using queue
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque([root])
        rv = []
        while queue: # each level a loop
            size = len(queue)
            rv.append(queue[-1].val)
            for _ in range(size): # pop and add nodes if there is any
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rv
