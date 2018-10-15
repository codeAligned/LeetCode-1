# 617. Merge Two Binary Trees
# Time:  O(N^k)
# Space: O(N^k)

# recursive merge left and right sub-trees until one tree is done
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return
        elif t1 and not t2 or not t1 and t2:
            return t1 or t2
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1