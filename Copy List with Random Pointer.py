# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# use a map to store the matching relation between the new list and the original list
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None

        head_cp = RandomListNode(head.label)
        p = head
        head_p = head_cp
        q = head_cp
        my_map = {head: head_cp}
        while p != None:

            q.random = p.random
            if p.next != None:
                q.next = RandomListNode(p.next.label)
                my_map[p.next] = q.next
            else:
                q.next = None
            q = q.next
            p = p.next

        p = head_p
        while p != None:
            if p.random != None:
                p.random = my_map[p.random]
            p = p.next
        return head_p


