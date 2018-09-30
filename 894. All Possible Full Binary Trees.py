# 894. All Possible Full Binary Trees
# Time: O(N^4)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        def build(N):
            if N == 1:
                return [TreeNode(0)]
            trees = []
            for i in range(1, N, 2):
                for x in build(i):
                    for y in build(N - 1 - i):
                        root = TreeNode(0)
                        root.left = x
                        root.right = y
                        trees.append(root)
            return trees
        
        if N % 2 == 0:
            return []
        return build(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        dp = {1: [TreeNode(0)]}
        i = 3
        while i <= N:
            new_trees = []
            for nodes, trees in dp.items():
                for left_tree in trees:
                    for right_tree in dp[i - 1 - nodes]:
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        new_trees.append(root)
            dp[i] = new_trees
            i += 2
            
        return dp[N]