class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums2 = nums[1:] + [nums[0]]
        return max(self.rob_one(nums), self.rob_one(nums2))

    def rob_one(self, nums):
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]

sol = Solution()
print sol.rob([4,5,7,8,3,9])