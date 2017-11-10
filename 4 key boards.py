class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N + 1)
        if N <= 3:
            return N
        dp[1], dp[2], dp[3] = 1, 2, 3
        cur_a = 1
        for i in range(2, N + 1):
            if dp[i - 3] * 2 >= dp[i - 1] + cur_a:
                dp[i] = dp[i - 3] * 2
                cur_a = dp[i - 3]
            else:
                dp[i] = dp[i - 1] + cur_a
        print dp
        return dp[N]
    def maxA2(self,N):
        dp = [0]*(N+1)
        for i in range(0, N+1):
            dp[i] = i
            for j in range(i-2):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        return dp[N]
sol = Solution()
print sol.maxA(10)
print sol.maxA2(10)