class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.curt = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curt is not None or len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        self.curt = self.stack.pop()
        nxt = self.curt
        self.curt = self.curt.right
        return nxt

root = TreeNode(1)
sol = BSTIterator(root)
print sol.next().val