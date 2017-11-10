# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root ==[]:
            return []
        res = []
        tmp_r = [root.val]
        cur_stack = [root]
        while len(cur_stack) != 0:
            res.append(tmp_r)
            tmp_r = []
            pre_stack = cur_stack
            cur_stack = []

            while pre_stack != []:
                cur = pre_stack.pop()
                if cur.left != None:
                    cur_stack.append(cur.left)
                    tmp_r.append(cur.left.val)
                if cur.right != None:
                    cur_stack.append(cur.right)
                    tmp_r.append(cur.right.val)
        return res



