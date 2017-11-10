# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        st = []
        if root == None:
            return []
        cur_l = [root]
        while len(cur_l) != 0:
            tmp = cur_l
            cur_l = []
            un_None = 0
            while len(tmp) != 0:
                node = tmp.pop(0)
                if node == 'null':
                    st.append(node)
                    continue
                st.append(node.val)

                if node.left != None:
                    cur_l.append(node.left)
                    un_None += 1
                else:
                    cur_l.append('null')
                if node.right != None:
                    cur_l.append(node.right)
                    un_None += 1
                else:
                    cur_l.append('null')
            while len(cur_l) > 0 and cur_l[-1] == 'null' and un_None== 0:
                cur_l.pop()
        return st

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        st_root = []
        head = None
        if len(data) == 0:
            return None
        else:
            node = data.pop(0)
            head = TreeNode(node)
            st_root.append(head)

        while len(data) != 0:
            node = data.pop(0)
            r_p = st_root.pop(0)
            if node != 'null':
                r_p.left = TreeNode(node)
                st_root.append(r_p.left)
            if len(data) != 0:
                node = data.pop(0)
                if node != 'null':
                    r_p.right = TreeNode(node)
                    st_root.append(r_p.right)
        return head





        # Your Codec object will be instantiated and called as such:
codec = Codec()
head = codec.deserialize([1,2,3,'null','null',4,5])
print codec.serialize(head)