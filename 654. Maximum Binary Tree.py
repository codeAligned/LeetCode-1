# 654. Maximum Binary Tree
# Time:  O(NlogN)
# Space: O(NlogN)

# recursive build Maximum Binary Tree for left and right sub-trees until nums is empty
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        max_i = 0
        max_num = float('-inf')
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_i = i
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        return root
