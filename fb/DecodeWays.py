class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        r2, r1 =1,1
        if len(s) == 0:
            return 0
        for i in range(1,len(s)):
            if s[i] == '0':
                r1 = 0
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                current = r2+r1
                r2 = r1
                r1 = current
            else:
                r2= r1
        return r1

sol = Solution()
res = sol.numDecodings('')
print res