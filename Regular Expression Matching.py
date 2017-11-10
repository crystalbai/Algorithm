class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0 and len(s) == 0:
            return True
        if len(p) == 0 and len(s) != 0:
            return False
        if len(s) == 0:
            if  len(p)>1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
        res = False
        if s[0] == p[0] or p[0] == '.':
            if len(p)>1 and p[1] == '*':
                return self.isMatch(s,p[2:]) or self.isMatch(s[1:],p)
            else:
                return self.isMatch(s[1:],p[1:])
        else:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
        return False
sol = Solution()
print sol.isMatch('aab', 'a*b')

