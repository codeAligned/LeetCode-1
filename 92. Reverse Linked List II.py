# 92. Reverse Linked List II
# Time: O(N)
# Space: O(1)

# iterative traverse linked list and reverse in place
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        left, mid, right = None, head, None
        front, m_node, n_node, back = None, None, None, None # use variables to track important nodes
        i = 1 # counter for m and n
        while mid:
            print(mid.val)
            if i == m - 1:
                front = mid
            if i == m:
                m_node = mid
            if i == n:
                n_node = mid
            if i == n + 1:
                back = mid
            if m <= i <= n: # reverse between m and n
                right = mid.next
                mid.next = left
                left = mid
                mid = right
            else: # move forward the mid cursor
                mid = mid.next
            i += 1
        
        if front: # point front node next pointer to n_node
            front.next = n_node
        else: # n_node could be the head of the list
            head = n_node
        m_node.next = back # point m_node next pointer to back node 

        return head
