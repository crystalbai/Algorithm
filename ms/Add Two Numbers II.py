# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        st1 = []
        st2 = []
        head = None
        tmp = None
        dig = 0
        while l1 != None:
            st1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            st2.append(l2.val)
            l2 = l2.next
        while len(st1) != 0 and len(st2) != 0:
            dig = st1.pop() + st2.pop() + dig
            carry = dig / 10
            dig = dig % 10
            head = ListNode(dig)
            head.next = tmp
            tmp = head
        if len(st1) != 0:
            dig = st1.pop() + dig
            carry = dig / 10
            dig = dig % 10
            head = ListNode(dig)
            head.next = tmp
            tmp = head
        if len(st2) != 0:
            dig = st2.pop() + dig
            carry = dig / 10
            dig = dig % 10
            head = ListNode(dig)
            head.next = tmp
            tmp = head
        return head
sol = Solution()
sol.addTwoNumbers()

