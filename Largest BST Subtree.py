class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if self.is_valid(root, -9999999, 9999999):
            return self.largestBSTSubtree(root.left) + 1 + self.largestBSTSubtree(root.right)
        else:
            return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def is_valid(self, root, min_val, max_val):
        if root == None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.is_valid(root.left, min_val, root.val) and self.is_valid(root.right, root.val, max_val)

sol = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)

print sol.largestBSTSubtree(root)