# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None:
            return True
        if s == None and t!=None:
            return False
        if s.val != t.val:
            res_tmp = False
            if s.left!=None:
                res_tmp = res_tmp or self.isSubtree(s.left, t)
            if s.right!=None:
                res_tmp = res_tmp or self.isSubtree(s.right,t)
            return  res_tmp
        else:
            res = self.tree_equal(s.left, t.left) and self.tree_equal(s.right, t.right)
            return res or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def tree_equal(self, s,t):
        if t == None and s == None:
            return True
        else:
            if t == None or s == None:
                return False
            if s.val == t.val:
                return self.tree_equal(s.left, t.left) and self.tree_equal(s.right, t.right)

root = TreeNode(3)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
# root.left.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right = TreeNode(5)
t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)
sol = Solution()
print sol.isSubtree(root, t)