# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # solution using DFS, but the order have some problems
    # def verticalOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     ans = {0:None}
    #     if root:
    #         ans[0] = [root.val]
    #         ans = self.addNode(root, ans, 0)
    #
    #     else:
    #         return []
    #
    #     l = []
    #     for i in range(min(ans),max(ans)+1):
    #         # if i > 0:
    #         #     ans[i] = ans[i][::-1]
    #         l.append(ans[i])
    #
    #     return l
    #
    #
    # def addNode(self, root, ans, d_center):
    #
    #     if root.left!= None:
    #         if ans.get(d_center-1) == None:
    #             ans[d_center-1] = [root.left.val]
    #         else:
    #             ans[d_center-1].append(root.left.val)
    #
    #     if root.right!= None:
    #         if ans.get(d_center+1) == None:
    #             ans[d_center+1] = [root.right.val]
    #         else:
    #             ans[d_center+1].append(root.right.val)
    #
    #     if root.left != None:
    #         ans = self.addNode(root.left, ans, d_center - 1)
    #     if root.right != None:
    #         ans = self.addNode(root.right, ans, d_center + 1)
    #     return ans
    def verticalOrder(selfself, root):
        #using WFS
        ans = {0:None}
        if root:
            q = [(root, 0)]
        else:
            return []
        while len(q)!= 0:
            if ans.get(q[0][1])== None:
                ans[q[0][1]] = [q[0][0].val]
            else:
                ans[q[0][1]].append(q[0][0].val)
            if q[0][0].left != None:
                q.append((q[0][0].left, q[0][1]-1))
            if q[0][0].right != None:
                q.append((q[0][0].right, q[0][1]+1))
            q.pop(0)
        l = []
        for i in range(min(ans),max(ans)+1):
            # if i > 0:
            #     ans[i] = ans[i][::-1]
            l.append(ans[i])

        return l



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(2)
root.right.left.left = TreeNode(5)
sol = Solution()
ans = sol.verticalOrder(root)
print ans