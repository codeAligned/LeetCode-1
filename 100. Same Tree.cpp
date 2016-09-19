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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL || q == NULL) 
            return (p == q);
        return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

// Time:  O(n)
// Space: O(n)

// stack and DFS pre-order traverse
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack<TreeNode *> stackP;
        stack<TreeNode *> stackQ;
        
        stackP.push(p);
        stackQ.push(q);
        
        while (!stackP.empty() && !stackQ.empty()) {
            TreeNode* tnP = stackP.top();
            TreeNode* tnQ = stackQ.top();
            stackP.pop();
            stackQ.pop();
            
            if (tnP && tnQ) {
                if (tnP->val != tnQ->val)
                    return false;
                stackP.push(tnP->right);
                stackP.push(tnP->left);
                stackQ.push(tnQ->right);
                stackQ.push(tnQ->left);
            }
            
            if ((tnP && !tnQ) || (!tnP && tnQ))
                return false;
        }
        
        return stackP.empty() == stackQ.empty();
    }
};