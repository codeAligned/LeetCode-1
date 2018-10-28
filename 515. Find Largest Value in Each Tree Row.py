# 515. Find Largest Value in Each Tree Row
# Time: O(N)
# Space: O(N)

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# use level order traversal (bfs with queue) to get max value for each level
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        queue = deque([root]) if root else []
        while queue:
            size = len(queue)
            max_val = float('-inf')
            for _ in range(size):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_val)
        return res
