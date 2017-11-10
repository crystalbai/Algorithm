# Definition for singly-linked list.
from Queue import PriorityQueue
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #using basic data structure
    def mergeKLists_basic(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0 :
            return []
        while len(lists) > 1:
            lists.append(self.merge(lists[0],lists[1]))
            lists.pop(0)
            lists.pop(0)
        return lists[0]


    def merge(self, list_1, list_2):
        if list_1 == None:
            return list_2
        if list_2 == None:
            return list_1
        if list_1.val <= list_2.val:
            list_1.next = self.merge(list_1.next, list_2)
            return list_1
        if list_1.val > list_2.val:
            list_2.next = self.merge(list_1, list_2.next)
            return list_2

    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        if len(lists) == 0 :
            return []
        q = PriorityQueue()
        for l in lists:
            if l != None:
                q.put((l.val, l))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

sol = Solution()
Node1 = ListNode(1)
Node1.next = ListNode(7)
Node1.next.next = ListNode(13)
Node1.next.next.next = ListNode(14)
Node2 = ListNode(10)
Node2.next = ListNode(11)
Node2.next = ListNode(15)
Node3 = ListNode(2)
Node4 = ListNode(3)
Node5 = ListNode(6)
Node6 = ListNode(6)
l = [Node5, Node3,Node4, Node6]
res = sol.mergeKLists(l)
print res
