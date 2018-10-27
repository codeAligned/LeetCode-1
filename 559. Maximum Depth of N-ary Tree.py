# 559. Maximum Depth of N-ary Tree
# Time: O(log(N))
# Space: O(1)

from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# use level order (bfs with queue) to get tree height.
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        res = 0
        queue = deque([root]) if root else []
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
        return res
