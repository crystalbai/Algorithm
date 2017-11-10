class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## dynamic programming
        # sell end with sell, do not have stack in hand at day i
        # buy end with buy, have stack in hand at day i

        #sell[i] = max{sell[i - 1], buy[i-1] + prices[i]}
        #buy[i] = max{buy[i-1], sell[i-2] - prices[i]}
        if len(prices) == 0:
            return 0
        sell = [0]
        buy = [-prices[0]]
        for i in range(1,len(prices)):
            sell.append(max(sell[i - 1], buy[i - 1] + prices[i]))
            buy.append(max(buy[i - 1], sell[max(i - 2, 0)] - prices[i]))
        return sell[len(prices)-1]
