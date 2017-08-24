# Definition for a  binary tree node
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
        self.root = root
        self.curNode = root
        self.stack = []
        while self.curNode != None:
            self.stack.append(self.curNode)
            self.curNode = self.curNode.left


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)!= 0


    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None
        res = self.stack[-1]
        cur_node = self.stack.pop()
        if cur_node.right != None:
            cur_node = cur_node.right
            while cur_node != None:
                self.stack.append(cur_node)
                cur_node = cur_node.left

        return res.val


root = TreeNode(7)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(9)
sol = BSTIterator(root)
print sol.next()
print sol.next()
print sol.next()
print sol.next()
        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())