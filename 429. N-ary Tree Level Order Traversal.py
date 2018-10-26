# 429. N-ary Tree Level Order Traversal
# Time: O(N)
# Space: O(N)

from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# bfs using queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        queue = deque([root]) if root else []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(level)
        return res
