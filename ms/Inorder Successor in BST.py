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
        if root == None:
            return None
        else:
            self.pre = None
            self.sec = None
            self.dfs(root, p)
            return self.sec.val

    def dfs(self, root, p):
        print root.val
        if root.left != None:
            self.dfs(root.left, p)
        if self.pre == p:
            self.sec = root
        self.pre = root
        if root.right != None:
            self.dfs(root.right, p)

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print sol.inorderSuccessor(root, root.left.left.left)