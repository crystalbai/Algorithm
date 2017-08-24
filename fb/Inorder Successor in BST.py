# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = None
        if root == None or p == None:
            return []
        while root!=None:
            if root.val <= p.val:
                root= root.right
            else:
                cur = root
                root= root.left
        return cur

sol = Solution()
root = TreeNode(7)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
res = sol.inorderSuccessor(root, TreeNode(5))
print res
