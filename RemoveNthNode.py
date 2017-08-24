# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = head
        for i in range(n):
            if tmp.next == None:
                head = head.next
                return head
            tmp = tmp.next

        con_h = head
        while tmp.next!=None:
            con_h = con_h.next
            tmp = tmp.next
        con_h.next = con_h.next.next
        return head

sol = Solution()
tmp = ListNode(1)
head = tmp
tmp.next = ListNode(2)
tmp = tmp.next
tmp.next = ListNode(3)
tmp = tmp.next
tmp.next = ListNode(4)
tmp = tmp.next
tmp.next = ListNode(5)
sol.removeNthFromEnd(head,5)