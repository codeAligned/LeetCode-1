# 2. Add Two Numbers
# Time:  O(n)
# Space: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0;
        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next;
            l1 = l1.next if l1 else 0;
            l2 = l2.next if l2 else 0; 
        return dummy.next;