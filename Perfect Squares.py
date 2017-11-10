import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [pow(2,31) for i in range(n + 1)]
        for i in range(1,int(math.ceil(math.sqrt(n+1)))):
            dp[i * i] = 1
        for a in range(1,n+1):
            for b in range(0,int(math.ceil(math.sqrt(n+1 - a)))):
                dp[a + b * b] = min(dp[a] + 1, dp[a + b * b])
        return dp[n]

sol = Solution()
print sol.numSquares(6)