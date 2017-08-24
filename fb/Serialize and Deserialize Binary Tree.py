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
        q = []
        ans = ""+root.val
        count =0
        if root.left!= None:
            count+=1
            q.append(root.left)
        if root.right!= None:
            count+=1
            q.append(root.right)
        while len(q) > 0 and count > 0:
            ans = ans + ','
            if q[0] == None and count > 0:
                ans = ans + 'null'
                q.pop(0)

            elif q[0] !=None:
                ans = ans + q[0].val
                if q[0].left != None:
                    count+=1
                    q.append(q[0].left)
                else:
                    q.append(None)
                if q[0].right != None:
                    count+=1
                    q.append(q[0].right)
                else:
                    q.append(None)
                q.pop(0)
                count-=1
        return ans





    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        root = TreeNode(data[0])
        q = [root]
        d_sign = 0

        for idx, val in enumerate(data[1:]):
            if d_sign == 0:
                if val != 'null':
                    tmp = TreeNode(val)
                    q[0].left = tmp
                    q.append(tmp)
                d_sign =1
            else:
                if val != 'null':
                    tmp = TreeNode(val)
                    q[0].right = tmp
                    q.append(tmp)
                d_sign = 0
                q.pop(0)

        return root




codec = Codec()
res = codec.deserialize("1,2,3,null,null,4,5")
ans_str = codec.serialize(res)
print ans_str
# codec.deserialize(codec.serialize(root))