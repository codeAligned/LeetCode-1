# 101. Symmetric Tree
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order traversal and put child nodes in queue in a symmetric order
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root.left, root.right]) if root else []
        while queue:
            size = len(queue)
            for i in range(size//2):
                node1 = queue.popleft()
                node2 = queue.popleft()
                if not node1 and node2 or node1 and not node2:
                    return False
                if node1 and node2:
                    if node1.val != node2.val:
                        return False
                    queue.extend([node1.left, node2.right, node1.right, node2.left]) # put in a symmetric order
                # do nothing if both nodes are None

        return True


# Time: O(N)
# Space: O(logN)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS recursive find out symmetric, need to carry left and right to compare symmetric for each node
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        
        # pass in helper with symmetric order, 
        # compare left.left and right.right, compare left.right and right.left
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
