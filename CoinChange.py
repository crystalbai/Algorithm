import math
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if  amount == 0:
            return 0
        dp = [pow(2,31)]* (amount+1)
        for i in coins:
            dp[i] = 1
        for i in range(amount+1):
            for j in coins:
                dp[i] = min(dp[i], dp[i-j]+1)
        return -1 if dp[amount]> amount else dp[amount]

sol = Solution()
print sol.coinChange([1,2], 2)