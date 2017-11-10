import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(lambda: 0)
        for l in wall:
            brick = l[0]
            for i in l[1:]:
                d[brick] += 1
                brick += i
        res = 0
        for key in d:
            if d[key] > res:
                res = d[key]
        return len(wall) - res



sol = Solution()
print sol.leastBricks([[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]])