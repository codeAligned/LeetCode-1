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
        for lst in lists:
            if lst:
                heapq.heappush(heap, (lst.val, lst))
        
        dummy = cur = ListNode(0)
        while heap:
            min_lst = heapq.heappop(heap)[1]
            cur.next = min_lst
            cur = cur.next
            if min_lst.next:
                heapq.heappush(heap, (min_lst.next.val, min_lst.next))
            
        return dummy.next