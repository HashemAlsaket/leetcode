/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

public:
    int rec(TreeNode* node, int low, int high, int v){
        if (low <= node->val && node->val <= high){
            v += node->val;
        }
        if (node->val < low){
            node->left = NULL;
        }
        if (node->val > high){
            node->right = NULL;
        }
        if (node->left != NULL){
            v = rec(node->left, low, high, v);
        }
        if (node->right != NULL){
            v = rec(node->right, low, high, v);
        }
        return v;
    };

public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        int v = 0;
        
        v = rec(root, low, high, v);
        
        return v;
    }
};