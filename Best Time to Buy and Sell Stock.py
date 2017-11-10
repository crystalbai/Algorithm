class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        min_p = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            else:
                if prices[i] - min_p > res:
                    res = prices[i]-min_p
        return res

sol = Solution()
print sol.maxProfit([7, 1, 5, 3, 6, 4])