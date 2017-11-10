# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p,q = q, p
        if root.val >= p.val and root.val <= q.val:
            return root.val
        if root.val > q.val:
            if root.left!= None:
                return self.lowestCommonAncestor(root.left, p,q)
        else:
            if root.right!=None:
                return self.lowestCommonAncestor(root.right, p,q)
        return False

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print sol.lowestCommonAncestor(root, TreeNode(1), TreeNode(6))
