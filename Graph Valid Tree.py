import collections
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        d = collections.defaultdict(list)

        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        if len(edges) == 0:
            return n == 1
        s = set()
        cur = [0]
        while len(cur) != 0:
            tmp = cur
            cur = []
            while len(tmp) != 0:
                node = tmp.pop(0)
                if node in s:
                    return False
                s.add(node)
                cur+= d[node]
                for key in d[node]:
                    d[key].remove(node)
        return len(s) == n
sol = Solution()
print sol.validTree(5,[[0,1],[0,2],[2,3],[2,4]])