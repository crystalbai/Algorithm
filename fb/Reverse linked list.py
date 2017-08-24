# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
