class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for n in range(2, len(s)+1):
            is_True = False
            if len(s)%n == 0:
                is_True = True
                s_l = len(s)/n
                for i in range(1,n):
                    if not s[i*s_l:(i+1)*s_l] == s[:s_l]:
                        is_True = False
                        break
            if is_True:
                return True
        return False


sol = Solution()
print sol.repeatedSubstringPattern("bbbb")