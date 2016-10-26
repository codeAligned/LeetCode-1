# 23. Merge k Sorted Lists
# Time:  O(nlogk)
# Space: O(k)

# Heap solution.
import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        
        dummy = cur = ListNode(0)
        while heap:
            ml = heapq.heappop(heap)[1]
            cur.next = ml
            cur = cur.next
            if ml.next:
                heapq.heappush(heap, (ml.next.val, ml.next))
            
        return dummy.next
            