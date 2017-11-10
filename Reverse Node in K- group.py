# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start.next:
            end = start
            for i in range(k):
                end = end.next
                if end == None:
                    return dummy.next
            tmp_next = end.next
            res = self.reverse(start.next, end)
            start.next = res[0]
            res[1].next = tmp_next
            start = res[1]
        return dummy.next

    def reverse(self, start, end):
        tmp1 = start.next
        start.next = None
        end.next = None
        head = start
        if start == end:
            return start
        if tmp1 == end:
            end.next = start
            return [end, start]
        while tmp1 != None:
            tmp2 = tmp1.next
            tmp1.next = head
            head = tmp1
            tmp1 = tmp2
        return [end, start]



head = ListNode(0)
head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(4)
sol = Solution()
print sol.reverseKGroup(head, 2)