class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        #recursive search but use dp to remember the states
        self.dp = [{} for i in range(len(nums) + 1)]
        self.dfs(nums, 0, S)
        return self.dp[0][S]

    def dfs(self, nums, start, S):
        if (start == len(nums)):
            return S==0

        if S in self.dp[start]:
            return self.dp[start][S]
        if len(nums) > 0:
            s1 = self.dfs(nums, start + 1, S - nums[start])
            s2 = self.dfs(nums, start + 1, S + nums[start])
        self.dp[start][S] = s1+s2
        return self.dp[start][S]

sol = Solution()
print sol.findTargetSumWays([1,0],1)