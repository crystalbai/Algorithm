# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        st = []
        order = []
        head = root
        if root == None:
            return 0
        while head != None or len(st) != 0:
            while head != None:
                st.append(head)
                head = head.left
            cur = st.pop()
            order.append(cur)
            head = cur.right
            if len(order) == k:
                return cur.val
        return None



sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print sol.kthSmallest(root, 2)
