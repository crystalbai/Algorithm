# Definition for a binary tree node.

import copy
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
        level = 0
        res = []
        cur_stack = [root]
        next_stack = []
        if root.val == None:
            return []
        while len(cur_stack)!=0:
            res_tmp = []

            while len(cur_stack) != 0:
                cur_node = cur_stack.pop(0)
                res_tmp.append(cur_node.val)
                if cur_node.left!=None:
                    next_stack.append(cur_node.left)
                if cur_node.right!=None:
                    next_stack.append(cur_node.right)
            res.append(res_tmp)
            cur_stack = next_stack
            next_stack = []

        return res

root = TreeNode(7)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(9)
sol = Solution()
print sol.levelOrder(root)