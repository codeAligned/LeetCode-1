// 297. Serialize and Deserialize Binary Tree
// Time:  O(n)
// Space: O(n)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        helper1(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        return helper2(in);
    }
    
private:
    void helper1(TreeNode* root, ostringstream& out) {
        if (root) {
            out << root->val << ' '; // preorder traverse
            helper1(root->left, out);
            helper1(root->right, out);
        } else {
            out << "$ ";
        }
    }

    TreeNode* helper2(istringstream& in) {
        string val;
        in >> val;
        if (val == "$")
            return NULL;
        TreeNode* root = new TreeNode(stoi(val));
        root->left = helper2(in);
        root->right = helper2(in);
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));