// 19. Remove Nth Node From End of List
// Time: O(N)
// Space: O(N)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
// use extra arraylist to store each listnode
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null && n == 1)
            return null;
        List<ListNode> al = new ArrayList<>();
        ListNode cur = head;
        while (cur != null) {
            al.add(cur);
            cur = cur.next;
        }
        int len = al.size();
        if (n == len)
            head = head.next;
        else if (n == 1)
            al.get(len - 2).next = null;
        else
            al.get(len - 1 - n).next = al.get(len + 1 - n);
        return head;
    }
}


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
// make a gap n between fast and slow pointers 
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        ListNode fast = dummy, slow = dummy;
        dummy.next = head;
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
