// 141. Linked List Cycle
// Time: O(N)
// Space: O(1)

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
// use fast and slow pointers to check cycle
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null)
            return false;
        ListNode fast = head, slow = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow)
                return true;
        }
        return false;
    }
}