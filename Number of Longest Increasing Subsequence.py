# import numpy as np
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dx = [1] * len(nums)  ## for the max length
        dz = [1] * len(nums)  ## for the instance
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dx[i] < dx[j] + 1:
                        dx[i] = dx[j] + 1
                        dz[i] = dz[j]
                    elif dx[i] == dx[j] + 1:
                        dz[i] += dz[j]
        max_l = max(dx)
        res = 0
        for i in range(n):
            if dx[i] == max_l:
                res += dz[i]
        return res

sol = Solution()
print sol.findNumberOfLIS([1,3,5,4,7])


