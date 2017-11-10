class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lft = [0]*len(height)
        min_l = 0
        min_r = 0
        r = [0]*len(height)

        res = [0]*len(height)
        for i in range(len(height)):
            lft[i] = min_l
            r[-i-1] = min_r
            min_l = max(min_l, height[i])
            min_r = max(min_r, height[-i-1])

        for i in range(len(height)):
            res[i] = max(min(lft[i], r[i]) - height[i],0)
        return sum(res)

sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])