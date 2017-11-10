class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        if n == 0:
            return 0
        dp = [[False for i in range(n)] for j in range(n)]
        dp[0][0] = True
        for j in range(0, n):
            dp[j][j] = True
            for i in range(j+1):
                if j-1 <= i+1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j]== True:
                    res+=1
        return res
sol = Solution()
print sol.countSubstrings("abc")