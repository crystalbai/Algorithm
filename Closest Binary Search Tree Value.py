# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import math
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = math.pow(2.0,64)
        cur = root
        while cur != None and target != cur.val:
            if abs(target-res) > abs(target-cur.val):
                res = cur.val
            if target < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if cur != None and target == cur.val:
            return cur.val
        return  res
sol = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
print sol.closestValue(root, 3.13)