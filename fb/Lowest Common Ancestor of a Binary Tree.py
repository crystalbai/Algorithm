# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        #use map to remember the parent of each node and trace back
        #when we found all the node, we only need to iterate until we found all the node:
        parent = {root:None}
        stack = [root] #dfs the tree
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left != None:
                stack.append(node.left)
                parent[node.left] = node
            if node.right != None:
                stack.append(node.right)
                parent[node.right] = node


        #push all p ancestor in a set
        p_ances = set([p])
        while parent[p] != None:
            p_ances.add(parent[p])
            p = parent[p]
        while q not in p_ances:
            q = parent[q]
        return q

root = TreeNode(3)
root.right = TreeNode(5)
# root.right = TreeNode(1)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)
sol =Solution()
print sol.lowestCommonAncestor(root,root,root.right).val
