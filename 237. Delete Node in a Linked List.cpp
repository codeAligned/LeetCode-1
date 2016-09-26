// Time: O(1)
// Space: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode *nextNode;
        nextNode = node->next;
        node->val = nextNode->val;
        node->next = nextNode->next;
        free(nextNode);
    }
};