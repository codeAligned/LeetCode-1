// 98. Validate Binary Search Tree
// Time: O(N)
// Space: O(N)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// preorder traversal
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        bool left = true;
        if (root != NULL) {
            return helper(root->left, LONG_MIN, root->val, left) && helper(root->right, root->val, LONG_MAX, !left);
        } else {
            return true;
        }
    }
    
    bool helper(TreeNode* root, long min, long max, bool left) {
        if (root != NULL) {
            if (left) {
                if (root->val < max && root->val > min) {
                    cout << root->val << endl;
                    return helper(root->left, min, root->val, left) && helper(root->right, root->val, max, !left);
                } else {
                    return false;
                }
            } else {
                if (root->val < max && root->val > min) {
                    cout << root->val << endl;
                    return helper(root->left, min, root->val, !left) && helper(root->right, root->val, max, left);
                } else {
                    return false;
                }
            }
        } else {
            return true;
        }
    }
};