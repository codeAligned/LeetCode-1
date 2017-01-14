// 206. Reverse Linked List
// Time: O(N)
// Space: O(1)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
// use three pointers to reverse
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode left = null, mid = head, right = null;
        while (mid != null) {
            right = mid.next;
            mid.next = left;
            left = mid;
            mid = right;
        }
        return left;
    }
}