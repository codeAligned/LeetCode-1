# 536. Construct Binary Tree from String
# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# recursive build tree2str, attention to no left only right case.
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        left_p_idx = s.find('(')
        if left_p_idx == -1:
            return TreeNode(int(s))
        root = TreeNode(int(s[:left_p_idx]))
        cnt, start = 0, left_p_idx
        for i in range(left_p_idx, len(s)):
            if s[i] == '(':
                cnt += 1
            if s[i] == ')':
                cnt -= 1
            if cnt == 0 and start == left_p_idx:
                root.left = self.str2tree(s[start+1:i])
                start = i + 1
            elif cnt == 0:
                root.right = self.str2tree(s[start+1:i])
        return root
