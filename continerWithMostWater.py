class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max = 0
        # # height = list(set(height))
        # for i in range(len(height)):
        #     for j in range(i+1, len(height),1):
        #         tmp = min(height[i] ,height[j]) * (j - i)
        #         if  tmp > max:
        #             max = tmp
        # return max
        res = 0;
        l = 0; r = len(height)-1
        while l < r:
            res = max(min(height[l], height[r]) * (r - l),res)
            if height[l] < height[r]:
                l+=1
            elif height[l] >= height[r]:
                r-=1
        return res



sol = Solution()
l = [1,1]
res = sol.maxArea(l)
print res