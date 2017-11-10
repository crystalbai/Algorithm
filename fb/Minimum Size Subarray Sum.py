import numpy as np
class Solution(object):
    def minSubArrayLen_dp(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = np.zeros((l+1,l+1))
        if l == 0:
            return 0
        for l in range(len(nums)):
            for i in range(len(nums) - l):
                if l == 0:
                    dp[i, i+l] = nums[i]
                    if dp[i,i+l] == s:
                        return l+1
                else:
                    dp[i, i+l] = dp[i,i+l-1] +nums[i+l]
                    if dp[i, i+l] == s:
                        return l+1

        return 0

    def minSubArrayLen(self, s, nums):
        r , l = 0,0
        res = -1
        tmp_sum = 0
        while r < len(nums) and l <= r:
            if tmp_sum < s:

                tmp_sum = tmp_sum + nums[r]
                r+=1

            while tmp_sum >= s:
                if res > r -l or res == -1:
                    res = r - l

                tmp_sum = tmp_sum - nums[l]
                l += 1
        if res == -1:
            return 0
        else:
            return res





sol = Solution()
print sol.minSubArrayLen(7, [2,3,1,2,4,3])