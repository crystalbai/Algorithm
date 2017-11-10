class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        st = [root]
        un_none = 1
        while len(st)!=0 and un_none != 0:
            cur = st
            st = []
            un_none = 0
            while len(cur)!= 0:
                node = cur.pop(0)
                if node == 'null':
                    continue
                if node.left != None:
                    st.append(node.left)
                    un_none +=1
                else:
                    st.append('null')
                if node.right != None:
                    st.append(node.right)
                    un_none +=1
                else:
                    st.append('null')
            ## check curlayer
            i , j = 0, len(st)-1
            while i < j:
                if (st[i] == 'null' and st[j] != 'null') or(st[i] != 'null' and st[j] == 'null'):
                    return False
                if st[i] == 'null' and st[j] == 'null':
                    i += 1
                    j -= 1
                    continue
                if st[i].val != st[j].val:
                    return False
                i+=1
                j-=1
        return True

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

res = sol.isSymmetric(root)
print res