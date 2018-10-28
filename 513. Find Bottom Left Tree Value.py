# 513. Find Bottom Left Tree Value
# Time: O(N)
# Space: O(N)

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# level order traversal (using bfs with queue) and get the first node of each level
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        queue = deque([root]) if root else []
        while queue:
            size = len(queue)
            res = queue[0].val
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return res
