# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    res = True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.get_maxAmin(root)
        return self.res

    def get_maxAmin(self, root):
        ## return max, min

        if root == None:
            return None

        if self.res and root.left != None:
            min_val = self.get_maxAmin(root.left)[1]
            self.res = self.res and min_val < root.val
        else:
            min_val = root.val
        if self.res and root.right != None:
            max_val = self.get_maxAmin(root.right)[0]
            self.res = self.res and max_val > root.val
        else:
            max_val = root.val
        return max_val, min_val


class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = True
        if root == []:
            return res
        if root.left != None:
            res = res and (root.val > self.get_maxAmin(root.left)[0]) and self.isValidBST(root.left)
        if root.right !=None:
            res = res and (root.val <self.get_maxAmin(root.right)[1]) and self.isValidBST(root.right)
        return res
    def get_maxAmin(self, root):
        ## return max, min

        if root.left != None:
            min_val = self.get_maxAmin(root.left)[1]
        else:
            min_val = root.val
        if root.right != None:
            max_val = self.get_maxAmin(root.right)[0]
        else:
            max_val = root.val
        return max_val, min_val



sol = Solution()
root = TreeNode(5)
root.left = TreeNode(14)
# root.right = TreeNode(10)
root.left.left = TreeNode(1)
# root.left.right = TreeNode(8)
print sol.isValidBST(root)

