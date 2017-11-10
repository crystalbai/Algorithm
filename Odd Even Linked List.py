# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        tmp_h1 = dummy1
        dummy2 = ListNode(0)
        tmp_h2 = dummy2
        while head != None:
            dummy1.next = head
            head = head.next
            dummy1 = dummy1.next
            if head != None:
                dummy2.next = head
                dummy2 = dummy2.next
                head = head.next
        dummy2.next = None
        dummy1.next = tmp_h2.next
        return tmp_h1.next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sol = Solution()
sol.oddEvenList(head)


