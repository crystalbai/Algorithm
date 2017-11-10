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
        if head == None:
            return None
        helper = head.next
        head.next = None
        while helper!=None:
            tmp = helper.next
            helper.next = head
            head = helper
            helper = tmp


        return head

sol = Solution()
head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(6)
print sol.reverseList(head)

