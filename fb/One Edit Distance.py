class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## make len(s) always > len(t), to avoid delete
        if len(s) == 0 and len(t) == 0:
            return False
        if len(s) < len(t):
            return self.isOneEditDistance(t,s)
        i = 0; j = 0
        while (i < len(s) and j < len(t)):
            if s[i]!= t[j]:
                return s[i+1:] == t[j:] or s[i+1:] == t[j+1:]
            i+=1; j+=1
        return (len(s) - len(t) ==1)

sol = Solution()
res = sol.isOneEditDistance('','s')
print res

