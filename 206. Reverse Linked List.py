# 206. Reverse Linked List
# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# need three variables to track the left, current, and right nodes
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left, cur, right = None, head, None 
        while cur:
            right = cur.next
            cur.next = left
            left = cur
            cur = right
        return left
