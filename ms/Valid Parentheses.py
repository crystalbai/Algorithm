class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        l = ['(','{','[']
        left = set(l)
        d = {')':'(', ']':'[','}':'{'}
        for i in s:
            if i in left:
                st.append(i)
            else:
                if len(st) != 0:
                    if d[i] == st[-1]:
                        st.pop()
                else:
                    return False
        return len(st)==0

sol = Solution()
print sol.isValid("()")