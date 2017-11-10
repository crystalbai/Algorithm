class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        col = len(dungeon[0])
        dp = [[0 for i in range(col)] for j in range(row)]
        dp[row - 1][col - 1] = max(1 - dungeon[row - 1][col - 1], 1)
        for i in range(col - 2, -1, -1):
            dp[row - 1][i] = max(dp[row - 1][i + 1] - dungeon[row - 1][i], 1)
        for j in range(row - 2, -1, -1):
            dp[j][col - 1] = max(dp[j+1][col - 1] - dungeon[j][col - 1], 1)
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = max(min(dp[i][j + 1] - dungeon[i][j], dp[i + 1][j] - dungeon[i][j]), 1)
        return max(dp[0][0],1)
sol = Solution()
print sol.calculateMinimumHP([[1,-2,3],[2,-2,-2]])