import collections
import copy

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ## toplogical sort
        g = collections.defaultdict(list)
        for i in range(numCourses):
            g[i]
        in_dim = [0] * numCourses
        for e in prerequisites:
            g[e[1]].append(e[0])
            in_dim[e[0]] += 1
        ## every time add in_dim 0
        pre_len = 0
        # res = [i for i in range(numCourses) if in_dim[i] == 0 and i not in g]
        res = []
        while pre_len != len(g):
            pre_len = len(g)
            g_copy = copy.deepcopy(g)
            for key in g_copy:
                if in_dim[key] == 0:
                    res.append(key)
                    for next_key in g[key]:
                        in_dim[next_key] -= 1
                    del g[key]

        return res



sol = Solution()
print sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]
)