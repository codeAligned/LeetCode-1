# 206. Reverse Linked List
# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        left, mid, right = None, head, None
        while mid:
            right = mid.next
            mid.next = left
            left = mid
            mid = right
        return left