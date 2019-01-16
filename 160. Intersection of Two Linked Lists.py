# 160. Intersection of Two Linked Lists
# Time:  O(n)
# Space: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = []
        lb = []
        pa = headA
        pb = headB
        while pa or pb: # get to the back of the two linked lists
            if pa:
                la.append(pa)
                pa = pa.next
            if pb:
                lb.append(pb)
                pb = pb.next
        res = None
        while la and lb: # use two stacks to compare from the tail of two lists
            ta = la.pop()
            tb = lb.pop()
            if ta == tb:
                res = ta
            else:
                break
        
        return res
