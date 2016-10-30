# 98. Validate Binary Search Tree
# Time: O(N)
# Space: O(N)

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.helper(root.left, float('-inf'), root.val, True) and self.helper(root.right, root.val, float('inf'), False)
        else:
            return True
    
    def helper(self, root, min, max, left):
        if root:
            if min < root.val < max:
                if left:
                    print(root.val)
                    return self.helper(root.left, min, root.val, True) and self.helper(root.right, root.val, max, False)
                else:
                    print(root.val)
                    return self.helper(root.left, min, root.val, True) and self.helper(root.right, root.val, max, False)
            else:
                return False
        else:
            return True