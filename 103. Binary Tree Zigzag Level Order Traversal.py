# 103. Binary Tree Zigzag Level Order Traversal
# Time:  O(n)
# Space: O(n)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        dq = deque([root]) if root else []
        reverse_order = False
        while dq:
            size = len(dq)
            level = []
            for _ in range(size):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if reverse_order:
                level.reverse()
            res.append(level)
            reverse_order = not reverse_order
                    
        return res
