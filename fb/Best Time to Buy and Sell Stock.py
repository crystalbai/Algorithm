class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # ans = 0

        # buy one
        # for idx, p in enumerate(prices):
        #     #sell one
        #     for j in prices[idx:]:
        #         if j > p and j-p > ans:
        #             ans = j - p
        min_price = 1000000;
        max_pro = 0;
        for i in prices:
            min_price = min(i, min_price)
            max_pro = max(max_pro, i - min_price)
        return max_pro
sol = Solution()
l = [7, 1, 5, 3, 6, 4]
print sol.maxProfit(l)

