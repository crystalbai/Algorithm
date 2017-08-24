# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        tmp_str = ''
        if root != None:
            tmp_str = tmp_str + str(root.val)
            if root.left != None:
                self.dfs(res, tmp_str, root.left)
            if root.right != None:
                self.dfs(res, tmp_str, root.right)
            if root.left == None and root.right == None:
                res.append(tmp_str)
        # for s in res:
        #     tmp = ''
        #     for j in s:
        #         tmp = tmp + j + '->'
        #     o.append(tmp[:-2])

        return res

    def dfs(self, res, tmp_str, node):
        if node.left == None and node.right == None:
            tmp_str = tmp_str +'->'+ str(node.val)
            res.append(tmp_str)
        if node.left !=None:

            self.dfs(res, tmp_str +'->'+ str(node.val), node.left)
        if node.right !=None:
            self.dfs(res, tmp_str +'->'+ str(node.val), node.right)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
res = sol.binaryTreePaths(root)
print res

