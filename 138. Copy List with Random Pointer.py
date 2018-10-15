# 138. Copy List with Random Pointer
# Time: O(N)
# Space: O(N)

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# build mappings for original and new copied nodes
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodes_map = {}
        p = head
        new_list = None
        while p:
            if p not in nodes_map:
                nodes_map[p] = RandomListNode(p.label)
            # build next pointer
            if p.next:
                if p.next not in nodes_map:
                    nodes_map[p.next] = RandomListNode(p.next.label)
                nodes_map[p].next = nodes_map[p.next]
            # build random pointer
            if p.random:
                if p.random not in nodes_map:
                    nodes_map[p.random] = RandomListNode(p.random.label)
                nodes_map[p].random = nodes_map[p.random]
            # assign new list header node
            if not new_list:
                new_list = nodes_map[p]
            p = p.next
            
        return new_list


# Time: O(N)
# Space: O(1)

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# node1 -> copy_node1 -> node2 -> copy_node2
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # build new copied nodes
        cur = head
        while cur:
            cp_node = RandomListNode(cur.label)
            cp_node.next = cur.next
            cur.next = cp_node
            cur = cp_node.next
        
        # build random pointer for copied nodes
        cur = head
        while cur:
            cp_node = cur.next
            cp_node.random = cur.random.next if cur.random else None
            cur = cp_node.next
            
        # extract copied nodes to a new list
        cur = head
        new_list = None
        while cur:
            cp_node = cur.next
            if not new_list:
                new_list = cp_node
            cur.next = cp_node.next
            cur = cp_node.next
            cp_node.next = cur.next if cur else None
                  
        return new_list
            