class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## if tomorrow's price is higher than today, then buy and sell tomorrow, it could be the case we buy one and sell one the same day
        sum = 0
        if len(prices) == 0:
            return 0
        for i in range(len(prices)-1):
            sum = sum + max(0, prices[i+1]-prices[i])
        return sum
sol = Solution()
print sol.maxProfit([7, 1, 5, 3, 6, 4])