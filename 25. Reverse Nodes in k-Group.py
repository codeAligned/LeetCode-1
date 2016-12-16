# 25. Reverse Nodes in k-Group
# Time: O(N*k)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2: # no need to reverse
            return head
        
        cur = head
        prev = None # record last element of previous group
        while cur:
            for i in range(k): # mark header and tail and examine k
                if i == 0:
                    header = cur
                if i == k - 1:
                    tail = cur
                if cur:
                    cur = cur.next
                else:
                    return head

            # reverse linked list
            left, mid, right = cur, header, None
            for i in range(k):
                right = mid.next
                mid.next = left
                left = mid
                mid = right
            
            if prev: # update last element's next of previous group
                prev.next = tail
            else:
                head = tail
            prev = header # update last element of previous group

        return head