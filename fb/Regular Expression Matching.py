import numpy as np
class Solution(object):
    def isMatch_DFS(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # write a recursive solution
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) == 0 and len(p) != 0:
            if len(p) > 1 and p[-1] == '*':
                return self.isMatch(s,p[:-2])
            else:
                return False
        if len(s) != 0 and len(p) == 0:
            return False
        for i in reversed(range(len(p))):

            if p[i] == '*':
                # if len(s) == 1 :
                #     return (p[i - 1] == '.' or s[- 1] == p[i - 1] ) and self.isMatch(s[:-1], p[:-2])
                # if i > 1 and s[- 2] != s[- 1]:
                #     return (p[ i- 1] == '.' or s[ - 1] == p[i - 1] ) and self.isMatch(s[:-1], p[:-2])
                tmp1 = (self.isMatch(s[:-1], p) and (s[-1] == p[i-1] or p[i-1] == '.'))
                if tmp1 == True:
                    return True
                tmp2 = self.isMatch(s, p[:-2]) #matching one or zero
                # print tmp1
                # print tmp2
                return tmp1 or tmp2
            if p[i] == '.':
                return self.isMatch(s[:-1], p[:-1])
            else:
                return self.isMatch(s[:-1], p[:-1]) and s[-1] == p[i]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #DP solution
        dp = np.zeros((len(s) + 1,len(p) + 1))
        dp.astype(bool)
        # o matching zero
        if len(s) == 0 and len(p) == 0:
            return True
        dp[0][0] = True

        #when len(s) ==0
        for i in range(1,len(p),2):
            dp[0][i+1] = (p[i] == '*' and dp[0][i-1])
        #when len(p) ==0
        if len(s) > 0:
            dp[1:][0] = False

        #start dp equations
        for i in range(0,len(s)):
            for j in range(0, len(p)):
                if p[j] == '*':
                    # matching 0 or 1
                    dp[i+1][j+1] = (dp[i+1][j-1] or (dp[i][j+1] and (p[j-1] == s[i] or p[j-1] == '.')))
                else:
                    #matching current and before is matching
                    dp[i+1][j+1] = dp[i][j] and (p[j] == s[i] or p[j] == '.')

        return dp[len(s)][len(p)].item() ==1

sol = Solution()
res = sol.isMatch("aab", "b.*")
print res
