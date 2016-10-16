// 101. Symmetric Tree
// Time:  O(n)
// Space: O(1)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 // recursive DFS
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return root == NULL || isSymmetricHelper(root->left, root->right);
    }
    
    bool isSymmetricHelper(TreeNode* left, TreeNode* right) {
        if (left == NULL || right == NULL)
            return left == right;
        if (left->val != right->val)
            return false;
        return isSymmetricHelper(left->left, right->right) && isSymmetricHelper(left->right, right->left);
    }
};


// Time:  O(n)
// Space: O(n)

// queue and BFS level-order traverse
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) 
            return true;
        queue<TreeNode *> check;
        
        check.push(root->left);
        check.push(root->right);
        
        while (!check.empty()) {
            TreeNode *node1 = check.front();
            check.pop();
            TreeNode *node2 = check.front();
            check.pop();
            if ((!node1 && node2) || (node1 && !node2)) 
                return false;
            if (node1 && node2) {
                if (node1->val != node2->val) 
                    return false;
                check.push(node1->left);
                check.push(node2->right);
                check.push(node1->right);
                check.push(node2->left);
            }
        }
        
        return true;
    }
};

