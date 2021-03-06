# 236. Lowest Common Ancestor of a Binary Tree
# Time: O(N)
# Space: O(H)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # solution 1: dfs
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

    # solution2: record child parent pairs to find path to p and q
    # 			 add p's ancestors into set, then traverse ancestor
    #			 of q and find the first common ancestor
    # dfs using stack
	def lowestCommonAncestor(self, root, p, q):
	    stack = [root]
	    parent = {root: None}
	    while p not in parent or q not in parent:
	        node = stack.pop()
	        if node.left:
	            parent[node.left] = node
	            stack.append(node.left)
	        if node.right:
	            parent[node.right] = node
	            stack.append(node.right)
	    ancestors = set()
	    while p:
	        ancestors.add(p)
	        p = parent[p]
	    while q not in ancestors:
	        q = parent[q]
	    return q
