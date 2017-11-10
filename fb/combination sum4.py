import numpy as np
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 and target ==0:
            return 0
        dp = [0]* (target+1)
        dp[0] = 1
        for i in range(target+1):
            for n in nums:
                if i >= n:
                    dp[i] = dp[i]+dp[i-n]
        return dp[-1]

sol = Solution()
print sol.combinationSum4([4,2,1], 32)


