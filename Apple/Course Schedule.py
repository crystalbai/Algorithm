class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        m = {}
        for i in range(numCourses):
            m[i] = [0, []]
        for l in prerequisites:
            m[l[1]][1].append(l[0])
            m[l[0]][0] += 1
        cur_s, next_r = 0, len(m)
        while cur_s != next_r:
            cur_s = next_r
            for key in m.copy():
                if m[key][0] == 0:
                    for i in m[key][1]:
                        m[i][0] -= 1
                    del m[key]
            next_r = len(m)
        return len(m) == 0
sol = Solution()
print sol.canFinish(2,[[1,0]])
