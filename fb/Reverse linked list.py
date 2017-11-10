# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        tmp = head.next
        head.next = None
        while tmp.next != None:
            after = tmp.next
            tmp.next = head
            head = tmp
            tmp = after
        tmp.next = head
        head = tmp
        return head
    def reverse(self, start, end):
        tmp1 = start.next
        start.next = None
        head = start
        if tmp1 == end:
            return [end, start]
        while tmp1 != None:
            tmp2 = tmp1.next
            tmp1.next = head
            head = tmp1
            tmp1 = tmp2
        return [end, start]

sol = Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
print sol.reverse(head,head.next.next.next)