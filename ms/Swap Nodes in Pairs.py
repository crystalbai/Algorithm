# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        while p.next != None and p.next.next != None:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp

            p = p.next.next

        return dummy.next
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next= ListNode(3)
head.next.next.next= ListNode(4)
head = sol.swapPairs(head)
print head