// 111. Minimum Depth of Binary Tree
// Time: O(N)
// Space: O(N)

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// DFS for minimum sum
public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left != null && root.right == null) {
            return minDepth(root.left) + 1;
        }
        if (root.left == null && root.right != null) {
            return minDepth(root.right) + 1;
        }
        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}