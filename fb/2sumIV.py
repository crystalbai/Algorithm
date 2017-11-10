class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.pre = set()
        if root == None:
            return False
        return self.dfs(root, k)

    def dfs(self, root, k):
        res = False
        if k - root.val in self.pre:
            return True
        self.pre.add(root.val)
        if root.left != None:
            res = res or self.dfs(root.left, k)
        if root.right != None:
            res = res or self.dfs(root.right,k)
        return res