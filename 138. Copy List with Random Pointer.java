// 138. Copy List with Random Pointer
// Time: O(N)
// Space: O(N)

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
// first loop for node copy, second loop for pointer copy
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null)
            return null;
        Map<RandomListNode, RandomListNode> hm = new HashMap<>();
        RandomListNode node = head;
        while (node != null) {
            hm.put(node, new RandomListNode(node.label));
            node = node.next;
        }
        node = head;
        while (node != null) {
            hm.get(node).next = hm.get(node.next);
            hm.get(node).random = hm.get(node.random);
            node = node.next;
        }
        
        return hm.get(head);
    }
}