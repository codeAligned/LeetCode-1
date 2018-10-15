# 894. All Possible Full Binary Trees
# Time: O(N^4)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive build FBT until only one root node
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
            # given this many nodes
            for i in range(1, N, 2):
                # build all possible left sub-trees
                for x in build(i):
                    # build all possible right sub-trees
                    for y in build(N - 1 - i):
                        root = TreeNode(0)
                        root.left = x
                        root.right = y
                        trees.append(root)
            return trees
        
        if N % 2 == 0:
            return []
        return build(N)


# Time: O(N^4)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DP to track all possible FBT until N
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
            # given trees in current DP tables
            for nodes, trees in dp.items():
                # iterate for all left sub-trees
                for left_tree in trees:
                    # iterate for all right sub-trees
                    for right_tree in dp[i - 1 - nodes]:
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        new_trees.append(root)
            dp[i] = new_trees
            i += 2
            
        return dp[N]