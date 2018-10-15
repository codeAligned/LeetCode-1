# 23. Merge k Sorted Lists
# Time:  O(Nlogk)
# Space: O(k)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use heap to maintain the streaming max/min value
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
        
        cur = dummy = ListNode(0)
        while heap:
            min_l = heapq.heappop(heap)[1]
            cur.next = min_l
            cur = cur.next
            if min_l.next:
                heapq.heappush(heap, (min_l.next.val, min_l.next))
        return dummy.next
