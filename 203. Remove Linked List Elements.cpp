// Time: O(n)
// Space: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// pointer to pointer to remove lisked list node
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode **ptr = &head;
        while (*ptr) {
            ListNode *temp = *ptr;
            if (temp->val == val) {
                *ptr = temp->next;
                free(temp);
            } else
                ptr = &(temp->next);
        }
        return head;
    }
};